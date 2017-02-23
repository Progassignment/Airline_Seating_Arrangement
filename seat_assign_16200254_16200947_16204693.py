# AIRLINE RESERVATION SYSTEM
# ROHIT SINGH(16200947) ELPIDA BANTRA(16200254) LISHA GHOSH(16204693)
# MSC BUSINESS ANALYTICS

# Updated by Elpida
# *******************************************************Import libraries into python************************************************#
import numpy as np  # Import numpy
import pandas as pd  # Import pandas
import sqlite3 #Import sqlite database
import sys #Import sys for command line args

#set initial values for variables
connection = None
cursor = None

refused_pass = 0
sep_pass = 0

layout_column_names = ''
layout_rows = 0

# *******************************************************Create database connection***********************************************

# import the SQLite database
def db_connection():
    global connection, cursor
    connection = sqlite3.connect(sys.argv[1])  # Create connection object to link database
    cursor = connection.cursor()  # Create cursor object
    return connection, cursor


connection, cursor = db_connection()

# Updated by Lisha
# *******************************************************Retrieve and update database metrics*******************************************************#

# Function to retrieve metrics from the database
def retrieve_metrics():
    global cursor, refused_pass, sep_pass
    cursor.execute('SELECT * FROM metrics')  # retrieve data from metrics table
    row = cursor.fetchone()
    refused_pass = row[0]
    sep_pass = row[1]
    return

refused_pass = retrieve_metrics()

# Function to update metrics in the database
def metrics_update(connection):
    global cursor, refused_pass, sep_pass
    cursor.execute("update metrics " + \
                   " set passengers_refused= ?, passengers_separated= ?" \
                   , (refused_pass, sep_pass))  # update data in the metrics table
    connection.commit()
    print("Database updated. Thanks for booking!")
    return

# Function to fetch data from the rows_cols table in the database
def layout_rows_cols():
     global cursor, layout_rows, layout_column_names
     cursor.execute("SELECT * FROM rows_cols")
     row = cursor.fetchone()
     layout_rows = row[0]
     layout_column_names = str(row[1])
     return

# Updated by Rohit
# *******************************************************Flight seating layout********************************************************#

# Function to get total number of seats
def layout_get_total_seats():
    All_seats = []
    global cursor
    for row in cursor.execute('select row,seat from seating'):
        All_seats.append(row)
    return All_seats

All_Seats = layout_get_total_seats()

# Function to get available seats
def layout_get_available_seats():
    Avl_Seats = []
    global cursor
    for row in cursor.execute('select row, seat from seating where name = "" '):
        Avl_Seats.append(row)
    return Avl_Seats

Avl_Seats = layout_get_available_seats()

# Updated by Elpida
# Function to get number of columns in the airplane
def layout_get_cols(Avl_Seats, All_seats=layout_get_total_seats()):
    c_name = []
    for l in zip(*All_seats):
        b = set(l)
    col_name = c_name.append(b)
    max_cols = set(l)
    col_count = len(max_cols)
    return col_count, col_name

col_count, col_name = layout_get_cols(Avl_Seats, All_seats=layout_get_total_seats())

# Function to allocate seats in the database
def update_seat_allocation(passenger_name, num_row, num_col):
    global cursor, layout_column_names, connection
    cursor.execute("update seating " + \
                      " set name = ? " + \
                      " where row = ? and seat = ? " \
                      , (passenger_name, (num_row+1), layout_column_names[num_col-1]))
    connection.commit()
    return


# Function to get number of rows in the airplane
def layout_get_rows(Avl_Seats, All_seats):
    max_rows = np.array([max(Avl_Seats)])
    row_count_1 = max_rows[:, 0]
    row_count_2 = np.asscalar(row_count_1)
    row_count = np.int(row_count_2)
    return row_count


row_count = layout_get_rows(Avl_Seats, All_seats=layout_get_total_seats())

# Updated by Lisha
# Functions to create matrix of seating plan
# Create matrix according to number of rows and columns
def get_seat_layout(row_count, col_count):
    seat_layout = np.zeros((row_count, col_count + 1))  # Add additional column to keep count of available seats
    seat_layout[:, 0] = col_count
    return seat_layout


seat_layout = get_seat_layout(row_count, col_count)

def airplane_layout(row_count, col_count):
    seat_layout = get_seat_layout(row_count, col_count)
    available_seats = np.sum(seat_layout[:, 0])
    return available_seats


available_seats = airplane_layout(row_count, col_count)

# Updated by Rohit
# ****************************************************Passenger details**************************************************#

# Read booking data
global passenger_bookings
def read_csv():
    passenger_bookings = pd.read_csv(sys.argv[2], names=['passenger_name', 'passenger_count'])
    return passenger_bookings

passenger_bookings = read_csv()

# Function to allocate seats to passengers
def seat_allocation(col,row,available_seats, seat_layout):
    pass_count = row['passenger_count'] #create variable to store passenger count for each booking as given in csv
    global sep_pass

    # Adjacent seat allocation for passengers
    for all_rows in range(seat_layout.shape[0]):
        if (pass_count != 0 and seat_layout[all_rows][0] >= pass_count):  #1st col index
            for all_columns in range(seat_layout.shape[1]):
                if (seat_layout[all_rows][all_columns] == 0):
                    seat_layout[all_rows][all_columns] = col #row and column index of where seat is to be allocated
                    pass_count -= 1 #decrement passenger count by 1 since passenger has been allocated a seat
                    available_seats -= 1 #decrement avaialble seats by 1 as one seat has been allocated
                    seat_layout[all_rows][0] -= 1 #decrement index count by 1 everytime a seat is allocated
                    update_seat_allocation(row['passenger_name'],all_rows, all_columns) #update seat allocation in the database

                if pass_count == 0:
                   break

    # Seat allocation when adjacent seating is not possible
    if (pass_count == row['passenger_count']):
         last_row = 0
         for all_rows in range(seat_layout.shape[0]):
             if (pass_count != 0 and seat_layout[all_rows][0] != 0):
                 for all_columns in range(seat_layout.shape[1]):
                     if (seat_layout[all_rows][all_columns] == 0):
                         if (pass_count == row['passenger_count']):
                             last_row = all_rows
                         seat_layout[all_rows][all_columns] = col #row and column index of where seat is to be allocated
                         pass_count -= 1 #decrement passenger count by 1 since passenger has been allocated a seat
                         available_seats -= 1 #decrement avaialble seats by 1 as one seat has been allocated
                         seat_layout[all_rows][0] -= 1 #decrement index count by 1 everytime a seat is allocated
                         update_seat_allocation(row['passenger_name'], all_rows, all_columns) #update seat allocation in the database

                         if (last_row != all_rows):
                             sep_pass +=1 # update separated passengers

                     if pass_count == 0:
                        break
    return available_seats, seat_layout

#program execution starts here
def main():
    if (len(sys.argv)==3): #Count number of arguments passed in the command line interface
        #sys.argv[0]= name of program
        #sys.argv[1]= name of database
        #sys.argv[2]= name of booking csv file
        global refused_pass
        global col
        global row
        global pass_count
        global available_seats, seat_layout
        global database
        #function calls
        db_connection()
        layout_get_total_seats()
        layout_get_available_seats()
        layout_get_cols(Avl_Seats, All_seats=layout_get_total_seats())
        layout_get_rows(Avl_Seats, All_seats=layout_get_total_seats())
        layout_rows_cols()
        airplane_layout(row_count, col_count)
        get_seat_layout(row_count, col_count)
        read_csv()
        retrieve_metrics()
        for col, row in passenger_bookings.iterrows():

            if available_seats >= row['passenger_count']:
                available_seats, seat_layout = seat_allocation(col+1,row,available_seats, seat_layout)
            else:
                refused_pass += row['passenger_count']
        print("Refused passengers: ",refused_pass)
        metrics_update(connection)

    else:
        print("Arguments passed in incorrect format")

    return

main() # Call to main function


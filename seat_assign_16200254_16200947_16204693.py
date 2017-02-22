
# AIRLINE RESERVATION SYSTEM
# ROHIT SINGH ELPIDA BANTRA LISHA GHOSH
# MSC BUSINESS ANALYTICS

#updated by Elpida
# *******************************************************Import libraries into python************************************************#
import numpy as np  # Import numpy
import pandas as pd  # Import pandas
import sqlite3
# initialization of objects
connection = None
cursor = None

refused_pass = 0
sep_pass = 0

FLIGHT_SEATS = ''
FLIGHT_NROWS = 0

# *******************************************************Create databse connection***********************************************

# import the SQLite database
def db_connection():
    global connection, cursor
    connection = sqlite3.connect('airline_seating.db')  # Create connection object to link databse
    cursor = connection.cursor()  # Create cursor object
    return connection, cursor


connection =db_connection()
#updated by Lisha
# *******************************************************Retrieve and update database metrics*******************************************************#
def retrieve_metrics():
    global cursor, refused_pass, sep_pass
    cursor.execute('SELECT * FROM metrics')  # retrieve data from metrics table
    row = cursor.fetchone()
    refused_pass = row[0]
    sep_pass = row[1]
    print(refused_pass, ",", sep_pass)
    
    # Function to create matrix of seating plan

def get_seat_layout(row_count, col_count):
    seat_layout = np.zeros((row_count, col_count + 1))  # Add additional column to keep count of available seats
    seat_layout[:, 0] = col_count
    return seat_layout


seat_layout = get_seat_layout(row_count, col_count)

def airplane_layout(row_count, col_count):
    seat_layout = get_seat_layout(row_count, col_count)
    available_seats = np.sum(seat_layout[:, 0])
    print("Available number of seats :")
    print(available_seats)
    print("Flight seat layout with available seats index")
    print(seat_layout)
    return available_seats


available_seats = airplane_layout(row_count, col_count)

    return


refused_pass = retrieve_metrics()


def update_metrics(connection):
    global cursor, refused_pass, sep_pass
    cursor.execute("update metrics " + \
                   " set passengers_refused= ?, passengers_separated= ?" \
                   , (refused_pass, sep_pass))  # update data in the metrics table
    connection.commit()
    return


def update_seat_allocation(passenger_name, num_row, num_col):
    global cursor, FLIGHT_SEATS, connection
#    print(booking_name, row_num+1, FLIGHT_SEATS[column_num-1])
    cursor.execute("update seating " + \
                      " set name = ? " + \
                      " where row = ? and seat = ? " \
                      , (passenger_name, (num_row+1), FLIGHT_SEATS[num_col+1]))
    connection.commit()
    return
#updated by Rohit
# *******************************************************Flight seating layout************************************************#
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
    # print ("Available seats are :")
    for row in cursor.execute('select row, seat from seating where name = "" '):
        Avl_Seats.append(row)
    # seats = np.array([Avl_Seats])
    return Avl_Seats


Avl_Seats = layout_get_available_seats()


# Function to get occupied seats
def layout_get_occupied_seats():
    Occ_Seats = []
    global cursor
    # print ("Occupied seats are :")
    for row in cursor.execute('select row, seat from seating where name != "" '):
        Occ_Seats.append(row)
    return Occ_Seats

#updated by Elpida
# Function to get number of columns in the airplane
def layout_get_cols(Avl_Seats, All_seats=layout_get_total_seats()):
    x = []
    for l in zip(*All_seats):
        b = set(l)
        print(b)
    max_cols = set(l)
    col_count = len(max_cols)
    return col_count


col_count = layout_get_cols(Avl_Seats, All_seats=layout_get_total_seats())


# Function to get number of rows in the airplane
def layout_get_rows(Avl_Seats, All_seats):
    max_rows = np.array([max(Avl_Seats)])
    row_count_1 = max_rows[:, 0]
    row_count_2 = np.asscalar(row_count_1)
    row_count = np.int(row_count_2)
    return row_count


row_count = layout_get_rows(Avl_Seats, All_seats=layout_get_total_seats())

# Updated by Lisha
# Function to create matrix of seating plan

def get_seat_layout(row_count, col_count):
    seat_layout = np.zeros((row_count, col_count + 1))  # Add additional column to keep count of available seats
    seat_layout[:, 0] = col_count
    return seat_layout


seat_layout = get_seat_layout(row_count, col_count)

def airplane_layout(row_count, col_count):
    seat_layout = get_seat_layout(row_count, col_count)
    available_seats = np.sum(seat_layout[:, 0])
    print("Available number of seats :")
    print(available_seats)
    print("Flight seat layout with available seats index")
    print(seat_layout)
    return available_seats


available_seats = airplane_layout(row_count, col_count)

#Updated by Rohit
#Function to read booking data
def read_csv():
    passenger_bookings = pd.read_csv('bookings.csv', names=['passenger_name', 'passenger_count'])
    #passenger_count = np.array([passenger_bookings['passenger_count']])
    #print(passenger_bookings)
    #print("Passenger count:")
    print(passenger_bookings['passenger_name'])
    return passenger_bookings

passenger_bookings = read_csv()

#Updated by Rohit
#Added logic for seat allocation

def seat_allocation(col,row,available_seats, seat_layout):
    #global available_seats
    pass_count = row['passenger_count']
    global sep_pass
    #print ("test")
    #print (row['passenger_count'])

    # Adjacent seat allocation for passengers
    for all_rows in range(seat_layout.shape[0]):
        if (pass_count != 0 and seat_layout[all_rows][0] >= pass_count):  #1st col index
            print(seat_layout[all_rows][0])
            for all_columns in range(seat_layout.shape[1]):
                if (seat_layout[all_rows][all_columns] == 0):

                    print(seat_layout[all_rows][all_columns])
                    seat_layout[all_rows][all_columns] = col
                    print("All rows")
                    print(all_rows)
                    print ("all cols")
                    print(all_columns)
                    print ("col")
                    print(col)
                    pass_count -= 1
                    print(pass_count)
                    available_seats -= 1
                    print(available_seats)
                    seat_layout[all_rows][0] -= 1
                    print(seat_layout)
                    update_seat_allocation(row['passenger_name'],all_rows, all_columns)
                    # print("Passe count")
                    # print(available_seats)
                    # print("Seat layout")

                if pass_count == 0:
                    #print(pass_count,available_seats,seat_layout[all_rows][0])
                   #print ("No more")
                   break

   #Book seats separately in case adjacent allocation is not possible
    if (pass_count == row['passenger_count']):
         print(col, "Adjacent booking is not possible")
         last_row = 0
         for all_rows in range(seat_layout.shape[0]):
             if (pass_count != 0 and seat_layout[all_rows][0] != 0):
                 for all_columns in range(seat_layout.shape[1]):
                     if (seat_layout[all_rows][all_columns] == 0):
                         if (pass_count == row['passenger_count']):
                             last_row = all_rows
                         seat_layout[all_rows][all_columns] = col
                         pass_count -= 1
                         available_seats -= 1
                         seat_layout[all_rows][0] -= 1
                         update_seat_allocation(row['passenger_name'], all_rows, all_columns)

                         if (last_row != all_rows):
                             #print(pass_count, available_seats, seat_layout[all_rows][0])
                             sep_pass +=1
                             print("sep")
                             print(sep_pass)

                     if pass_count == 0:
                         break
    return available_seats, seat_layout


# AIRLINE RESERVATION SYSTEM
# ROHIT SINGH ELPIDA BANTRA LISHA GHOSH
# MSC BUSINESS ANALYTICS
# Updated 20th Feb by Rohit Singh

# *******************************************************Import libraries into python************************************************#
import numpy as np  # Import numpy
import pandas as pd  # Import pandas
import sqlite3

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

# *******************************************************Retrieve and update database metrics*******************************************************#
def retrieve_metrics():
    global cursor, refused_pass, sep_pass
    cursor.execute('SELECT * FROM metrics')  # retrieve data from metrics table
    row = cursor.fetchone()
    refused_pass = row[0]
    sep_pass = row[1]
    print(refused_pass, ",", sep_pass)
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

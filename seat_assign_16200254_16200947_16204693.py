
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

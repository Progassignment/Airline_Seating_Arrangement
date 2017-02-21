
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

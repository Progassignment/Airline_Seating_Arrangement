
#AIRLINE RESERVATION SYSTEM
#ROHIT SINGH ELPIDA BANTRA LISHA GHOSH
#MSC BUSINESS ANALYTICS

import sqlite3 #import the SQLite database
connection = sqlite3.connect('airline_seating.db') #Create connection object to link databse
cursor = connection.cursor() #Create cursor object  

import numpy as np #Import numpy
import pandas as pd #Import pandas 

#Import all seats

All_seats = []
for row in cursor.execute('select row,seat from seating'):
        All_seats.append(row) 
#print(All_seats)
#print (a_seats[:,[0,1]])

x =[]
for l in zip(*All_seats):
    b=set(l)
    print(b)
   

 #Get number of columns in seating arrangement    
max_cols = set(l)
col_count = len(max_cols)
print ("The number of columns is : ")
print (col_count)


#Import details of Available and Occupied seats from db into python list

# import empty seats from table 'seating'
Avl_Seats = []
#print ("Available seats are :")
for row in cursor.execute('select row, seat from seating where name = "" '):
    Avl_Seats.append(row)
seats = np.array([Avl_Seats])
#print (seats)



#Calculate number of rows in the flight 

max_rows = np.array([max(Avl_Seats)])    
row_count = max_rows[:,0]
print ("The number of rows is :" )
print (row_count)

#print (seats[:,[0,1]])

    
#import occupied seats from table 'seating'
Occ_Seats = []
#print ("Occupied seats are :")
for row in cursor.execute('select row, seat from seating where name != "" '):
        Occ_Seats.append(row)
#print (Occ_Seats)

print ("Number of available seats are :")
print (len(Avl_Seats))
print ("Number of occupied seats are :")
print (len(Occ_Seats))


 
#csv = np.genfromtxt ('bookings.csv', delimiter=",")   
#print (csv)

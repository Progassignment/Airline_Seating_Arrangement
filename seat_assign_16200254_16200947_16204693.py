
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

# Functions for validation
def Read_csv(filename):
    Booking_Temp_df=pd.Read_csv(filename, names=['Booking_Name','Booking_Count'])
    return Bookings_Temp_df
    #Bookings_df= pd.read_csv(filename)

# Allocation of seats as booking comes in 
def Seat_Allocation(index, rows, Avl_Seats, All_seats):
    Booking_Count = rows['Booking_Count']

#    Allocations of seats side by side
    for row in range(All_Seats.shape[0]):
        if(Booking_Count!=0 and All_Seats[row][0]>=Booking_Count):
            for column in range(All_Seats.shape[1]):
                if(All_Seats[row][column]==0):
                    All_Seats[row][column]=index
                    Booking_Count -=1
                    Avl_Seats-=1
                    All_Seats[row][0]-=1
                if Booking_Count ==0:
#                    print(Booking_Count,Avl_Seats,All_Seats[row][0])
                    break
#    No Allocation done and book separately
    if(Booking_Count == rows['Booking_Count']):
        print(index,"Not possible to allocate side by side")
        for row in range(All_Seats.shape[0]):
            if(Booking_Count!=0 and All_Seats[row][0]!=0):
                for column in range(All_Seats.shape[1]):
                    if(All_Seats[row][column]==0):
                        All_Seats[row][column]=index
                        Booking_Count -=1
                        All_Seats-=1
                        All_Seats[row][0]-=1
                    if Booking_Count ==0:
#                        print(Booking_Count,Avl_Seats,All_Seats[row][0])
                        break
    
      return Avl_Seats,All_Seats

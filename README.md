# Airline_Seating_Arrangement
Business requirements and implementation

We started dealing with this problem according to the business demands. The specified requirements are : 
->The program should be able to read any db file in order to work with different airplane structures and with different seat allocations. To extract the airplane structure we have first linked the database with python creating an object using db_connection() function. We have extracted the data (rows and columns) of the seating arrangement in the form of a list. Next we extracted the data from the metrics table and updated the database with counts of refused passenger(refused_pass) and with passengers seating apart from their members(sep_pass). 

->Then it reads passenger details from csv files as they come in and allocate the available seats (if any). We read the csv file provided to us using read_csv() function.
Assumptions: The number of the passengers in each booking is an integer number than can greater than or equal to one.
After the connection between the database and code is established, we built different functions to allocate the seats to the passengers as the bookings come in (Flight Seating Layout section). In this part, firstly it is checked if there are available seats left for the upcoming booking. Next we check if there are adjacent seats left for allocation. Otherwise, they are allocated to the first available seat (row-wise). For this purpose, the rows were initially created with an extra column which is used as a counter and keep a track of the available number of seats at every row. This counter is also used for updating the available seats count in the database.

->The user of our program should be able to run it on the command line by typing python seat_assign_16200254_16200947_16204693.py
airline_seating.db bookings.csv. To implement this criteria we have imported the sys library in our code and checked ( if (len(sys.argv)==3)) for the command the line criteria in the main function before function executions start.If the criteria is satisfied the functions are called in the order in which they were defined.
At the end of the main function two metrics are updated: number of passengers that were refused allocation(refused_pass) and number of passengers that have been allocated away from any other member(sep_pass), in the database.

TEST CASES:
Given seating configuration:
NON-CORRUPTED csv files:
  a)There are no available seats - expected results
  b)no adjacent seat is available - expected results
  c) only adjacent seats are available - expected results
CORRUPTED csv file:
  a) EMPTY LINE (blank rows)- the output of the refused passengers was increasing the count according to blank rows. We tried to overcome    this error giving to our code in the read_csv function the skip_blank but it doesn't work.
  b) FLOATING TYPE inputs in the csv file - the output is the same as it had been given the floor of the decimals (integers). With 0       integer (similarly with a decimal positive and <0 ) the programm is not increasing the number of the refused passengers.
 c) NON-REAL INTEGERS and fractions-  Error:the program stops running. 
 d) NEGATIVE INTEGER- as the integers are not considered with their absolute values, the passenger (refused and adjacent) counts decrease according to negative number.
 e) bookings with the same passenger name- in this case the multiple entries of one name are considered (except for the initial name which is considered as unique and the booking is happening) as blank rows and we take the output of the case (a) of the corrupted files.

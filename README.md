# Airline_Seating_Arrangement
Business requirements and implementation

We started dealing with this problem detecting the business demands. The specified requirements are : 
->The program should be able to read any db file in order to work with different airplane structures and with different seat allocations. To extract the airplane sturucture we have first linked the database with python creating an object using db_connection() function. We have extracted the data (rows and columns) of the seating arrangement in form of list. next we have extracted the data from the metrics table and updated the database with counts of refused passenger(refused_pass) and with passengers seating apart from their members(sep_pas). 

->Then it should be able to read passengers bookings from csv files as they come in and allocate the available seats (if there are any to the passengers). We are reading the csv file provided to us using read_csv() function.
Assumptions: The number of the passengers in each booking is an integer number than can greater than or equal to one.
After the connection between the database and code is established, we built different functions to allocate the seats to the passengers as the bookings come in (Flight Seating Layout section). In this part, firstly it is checked if there are available seats left for the upcoming booking. Next we check if there are adjacent seats left for allocation. Otherwise, they are allocated to the first available seat (row-wise). For this purpose, the rows were initially created with an extra column which is used as a counter and keep a track of the available number of seats at every row. This counter is, also, used for updating the available seats count in the database.

->The user of our program should be able to run it on the command line by typing python seat_assign_12341234_56785678.py
data.db bookings.csv. To implement this criteria we have imported system in our code and ckecked ( if (len(sys.argv)==3)) for the command the line criteria before executing the main function.If the criteria is satisfied, the main function is executed and the functions are called in the order in which they were defined. 
At the end of the main function two metrics are updated: number of passengers that were refused allocation(refused_pass) and number of passengers that have been allocated away from any other member(sep_pass), in the database.

TEST CASES:
Given seating configuration:
i) There are no available seats
ii) no adjacent seat is available
iii) only adjacent seats are available
iv) corrupted csv file (empty line, non integer value)
And, also, a different db file was created to check the above four cases
with a different seating configuration for the above four cases

Results
Our code is working for all the above cases.

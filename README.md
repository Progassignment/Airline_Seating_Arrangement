# Airline_Seating_Arrangement
Business requirements and implementation

We started dealing with this problem detecting the business demands. Our program should be able to read any db file in order to work with different airplane structures and with different seat allocations primarily. We linked the database with python creating connection object using db_connection function and took the data from the database and created the lists row and col  for updating the metrics for refused passengers(refused_pass) and for passengers seating apart from their members(sep_pas). 

Then it should be able to read passengers bookings from csv files as they come in and allocate the available seats (if there are any to the passengers).
Assumptions: The number of the passengers in each booking is an integer number greater or equal to one.

After this, we built different functions to allocate the seats to the passengers as the bookings come in (Flight Seating part of the code). In this part, firstly it is checked if there are available seats left for the upcoming booking. Next we check if there are adjacent seats left for allocation. Otherwise, they are allocated to the first available seats (row-wise). For this purpose, the rows were initially created with an extra column which is a counter that represents the available number of seats at every row. This counter is, also, used for updating the available seats count.

In the main function, two metrics are updated: number of passengers that were refused allocation(refused_pass) and number of passengers that have been allocated away from any other member(sep_pass), in the database.

Finally, to check our code we created csv files that cover the following cases:
Given seating configuration:
i) there are no available seats
ii) no adjacent seat is available
iii) only adjacent seats are available
iv) corrupted csv file (empty line, non integer value)
And, also, a different db file was created to check the above four cases
with a different seating configuration for the above four cases

Results
Our code is working for all the above cases.

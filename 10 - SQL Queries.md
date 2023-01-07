HOW DO WE ACTUALLY RUN THESE QUERIES INSIDE THE SQL DATABASE?

In order to create a SQLite database which is just a file, we can start by simply creating a file. In the terminal, "touch flights.sql" will create a brand new file called "flights.sql". This by default has nothing in it.

To run it as a SQLite file, we can run "SQLite3 flights.sql" in the command line.

Now that we are in the SQLite prompt we can begin to write command lines that will be executed on this SQL database. 

Now we are creating a table called "flights" on the terminal. In order to access if the table is actually created, write ".tables" in the terminal. It will show the name of all the created tables currently in the database.

Although there is nothing in the table as when we type in "SELECT * FROM flights;" on the terminal, we get nothing, i.e., that is there is no data inside the table.

Now we can actually put data into this table. Now when we retrieve this data, we will get the information in the tables. ID is assigned automatically.

Now we add more data into the tables. If we want to make it more presentable then we can improve it by ".made columns" and ".headers yes" into the terminal. Now the data is organized more nicely in the terminal.

Now if we want unique rows then we can write "SELECT * FROM flights WHERE origin = "New York";" (here we will only get the flights where origin is New York.)

We can also write something like select the flights where duration is greater than 500 by "SELECT * FROM flights WHERE duration>300 AND destination="London";" (similarly we can use OR her instead of AND).

There are also other types of queries we can perform. Not only "=" is required, we can use other type of BOOLEAN expressions as well. For example: SELECT * FROM flights WHERE origin IN ("New York", "India");  [this selects all the flights whose origin is in either New York or India].

We can also write any query where the the data matches any particular pattern. That is used when you know a column looks a certain way but you don't know exactly what the value is. We may run a query like "SELECT * FROM flights WHERE origin LIKE "%a%";" [here we are looking at the values of a particular column, in this case, the value of the origin column which means that the percent stands for zero or more characters no matter what those characters are followed by "a" followed by more characters.]

You can also add additional functions in your SELECT queries. For example instead of just selecting values in a column, you can also find the average duration of flights by the usage of AVERAGE or count how many flights are coming to a particular destination by using COUNT or find the longest flight that goes to a particular destination MAX or the shortest flight that is taken to a particular destination MIN or add up all the durations to the whole bunch of flights SUM.

But in order to update data that is already inside the database we use UPDATE command.

UPDATE flights
    SET destination = "Paris"
    WHERE origin = "Washington DC"
    AND duration = 119;

In addition to updating and changing data we also need a command to delete data which is done by 

DELETE FROM flights WHERE destination = "Singapore";

We may also add other clauses in a particular Query, that is, we can LIMIT the results that come back. For example: SELECT * FROM flights LIMIT 5; [only 5 results come back] or ORDER BY allows me to decide how the results are ordered when they come back. For example: SELECT * FROM flights ORDER BY destination; or GROUP BY which allows us group a whole bunch of rows together. For example: SELECT * FROM flights GROUP BY origin;
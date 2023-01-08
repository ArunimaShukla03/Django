Now we would like to create a table inside a database by various SQL commands we can run on our database in order to perform various diferent operations.

In order to create a table:

CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

=> here the name of the table is "flights" then what is the parenthesis is a comma separated list of all of the columns that should be present in the table. This just decides the structure of the table and no data inside it is added yet. Here we have the name of the column written in small letters ("id", "origin", etc.). 

=> "id" is a unique identification given to each flight.

=> After the names of the columns in the table, its type is given after it (INTEGER, TEXT, etc.).

=> PRIMARY KEY is the primary way via which we can uniquely identify (here, flight). NOT NULL is a way to convey that the field should not be left empty. We don't ever want a flight that doesn't have an origin or destination, etc.

AUTOINCREMENT is a cue into SQL to automatically update the id every time we add a new row into the table.

We can add number of constraints in a particular column for example UNIQUE (makes sure that every value is going to be unique), CHECK (makes sure that a value obeys a certain condition), NOT NULL, DEFAULT.

HOW ARE WE GOING TO ADD DATA INTO THE TABLES?

We are going to do so via an INSERT command.

The command is generally going to look like:

INSERT INTO flights
    (origin, destination, duration)
    VALUES ("New York", "London", 415)

=> here we are adding a new row into the "flights" table. Here in paranthesis we are going to provide all the column names for which we are going to provide values. We should mind the order while giving the values for each column.

Although once we have added data into the table, we would also like a way to get data out of that table. For this we are going to write a particular type of query called the SELECT query.

WHAT DOES A QUERY LOOKS LIKE?

SELECT * FROM flights;

=> here this means that select all the possible columns in the "flights" table. The whole table is going to come back to me when we write this query.

WHAT HAPPENS IF WE DON'T NEED ALL THE DATA THAT IS WE ONLY WANT SELECTIVE DATA FROM THE TABLE?

SELECT origin, destination FROM flights;

=> here we are only selecting the "origin" and "destination" column from the table.

OR

SELECT * FROM flights WHERE id = 3;

=> only going to return the rows where id is 3.

OR

SELECT * FROM flights WHERE origin = "New York";

=> only going to return the rows where origin is New York.

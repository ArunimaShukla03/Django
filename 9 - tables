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
Django gets more interesting when we delve into the world of data and trying to have web applications that store data inside of a database.

SQL is a database language that we use to interact with databases and Django is going to allow us to have an abstraction layer on top of SQL.

To interact by not writing direct SQL queries but by interacting with Python classes and objects known as "models".

"Migrations" are going to be a technique that are going to allow us to update our database in response to changes that we make to our underlying models.

"Data" can be stored in various ways inside a computer system but generally in databases (particularly relational databases), we are going to store data inside a table where each table consists of rows and columns (here, we are going to construct a database and a web application that an airline may use)

SQL is a database language that is designed to interact with relational database management systems. Database that organises data into tables where every table consists of rows and columns. Some of the database management system includes MySQL, PostgreSQL, SQLite, etc. Each of these has different features and different use cases where some might be more appropriate than the other.

MySQL and PostgreSQL are more heavier database management system where they run on servers elsewhere while big companies use servers like this in order to store data and represent their data in sort of a separate database where the basic idea is that you have your web application running on one server while you want your database running as an entirely separate process. This is done so that both of them can be independent and while one catches bug, the whole system doesn't go down.

SQLite is the lighter weight implementation of the SQL standard. While it being rather than a server while accepts requests and returns appropriate responses, SQLite is going to store all of its data as a single file. 

As we begin storing data, each of that data has a type that represent various different categories of information that you might want to store inside a database. Each DBMS has its own set of data type where SQLite has text, integers, real numbers, numeric (number like data example a date), BLOB (binary large object like sequences of zeroes and ones that you might want to store inside your database like audio files or images).

MySQL has much longer list of other types of data such as Char(size) [takes an argument of size which is exact number of characters], Varchar(size) [takes an argument of size which is upto that number of characters], Smallint, Int, Bigint [change in number of bytes allocated], floar [a floating point number], double [uses more bytes of memory].
As we create these databases, there is a potential for threat too, where a key one to be aware of is known as "SQL Injection Attack".

This is a security vulnerability that can happen if you are not careful about how you execute your SQL commands.

So, when we log in a particular website, we use the SQL command:

SELECT * FROM users WHERE username = "Harry" AND password = 12345;

Now we get all the information of this user and we are successfully logged in the website. 

But here something that a hacker might do is put Hacker"-- as their password which makes the SQL query a comment now as -- in SQL identifies a comment, thus it makes the hacker bypass the password check allowing them to log in to the website even if they were unauthorized to do so.

SELECT * FROM users WHERE username = "Hacker"--" AND password = "";

HOW DO WE SOLVE THIS PROBLEM?

One way to solve this is to escape these characters by adding some backslashes just to make sure that SQL treats them as a literal quotation marks and a literal dash and not special SQL syntax of any sort. 

Another strategy is to use an abstraction layer on top of SQL so that we don't have to use SQL queries at all which is what we are about to do as we are about to transition to Django. 

One of the other concern worth noting about with regards to SQL is the possibility of race conditions.

A race condition is something that might happen when you have multiple events that are happening in the parallel threads, i.e., when you have one thing and the other thing happening simultaneously.

For example: on social media sites when you can like a post like an image on instagram or a tweet on twitter. What would happen if two people like the same post at the same time?

If we are not careful about those SQL queries then there's a potential to get into race condition problems when one person tries to query the number of likes that post has and when another person does the same thing, we have conflicts when we try and update it.

One strategy to solve this issue is to put a lock on the database that if I am working on this database, nobody can touch this data, while I am working nobody touches it, but when I am done, I can sort of release the lock and let someone else modify the database as well.

Now that we know the basic structure of the SQL queries, we would like to use the power of Django in order to design our web application by representing this data in terms of these models.
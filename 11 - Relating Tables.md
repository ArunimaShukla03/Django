Generally in our database we have multiple tables that are related to each other in some way. Where we would need something called "Foreign Keys".

For example: when writing the origin from a particular city, it might not be suitable as one city has multiple airports, then we need to have something like airport codes to identify which airport we are talking about. Now if we add codes,the table is getting fairly large.

So when we have larger and larger data, we want to separate this data into different tables that just reference one another in some way. So instead of having just "flights" table, another type of object we care about is "airports". 

Now this has three columns such as the id of the airport (unique number), one column for the three letter code for that airport and another for the city where the airport is in.

Now that we have a separate table, instead of storing an origin and the destination as text, we can store a "foreign key". A reference to a key in another table and rename those columns to "origin_id" and "destination_id" which instead of text will store a number. 

Now we have origin_id and destination_id stored as the id from another table where we can see which airport has what id and then replace them in the "flights" table.

We are combining now 2 tables, one representing "flights" and the other the "airports" and we are connecting these two tables by a foreign key.

Now as our database grows, this ability to relate data to one another becomes extremely powerful. Now in addition to storing airports and storing flights, an airline also might want to store the information about its passengers. 

Now we have also a table with passengers which have an id column to uniquely identify each passenger, a first name column, a last name column and flight_id column for storing what flight they would be on which takes its information from the "flights" table stating where is flight's origin and destination with its duration.

But here in the passengers table, there is a limitation on the table design we have created, i.e., any particular row can only have on flight_id associated with it.

Therefore, we have different type of relationships between rows, one such type of relationship is "many to one relationship" or "one to many relationship", i.e., one flight can be associated with many different passengers. But we might also want a "many to many relationship" where many different passengers can be associated with many different flights. A passenger may have more than one flight and vice-versa.

For doing this we need a different type of structure. One way to do this is just simply storing "people" in a table instead of "passengers" where every person has an id, a first name and a last name. But we are no longer storing flight information inside this table. 

Thus we create now another table that only has the "person_id" and a "flight_id". Where a person with a person_id is associated with a flight and we can repeat the same person to now different number of flights. But now our tables are not as clear as it is not immediately obvious to me, when I look at this table, what data I am looking at.
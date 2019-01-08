# Logs-Analysis
An SQL querying program for Udacity's Full stack nanodegree  

## Design
The design is straightforward, other than the SQL queries. The program connects
to the database, makes a query, and gets a cursor in return. It then addresses
each row of the cursor individually, breaks apart the tuple into variables assigned
to each column, and prints the row in more readable form, before moving on to the
next row. When it finishes with a cursor, it moves on to the next query.

# Logs-Analysis
An SQL querying program for Udacity's Full stack nanodegree  

## Design
The design is straightforward, other than the SQL queries. The program connects
to the database, makes a query, and gets a cursor in return. It then addresses
each row of the cursor individually, breaks apart the tuple into variables assigned
to each column, and prints the row in more readable form, before moving on to the
next row. When it finishes with a cursor, it moves on to the next query.  

## Instructions

Download the data from this link: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip  
Unzip the file, pull the "newsdata.sql" file out, and put it into a vagrant file
used to spin up a virtual machine on your computer on which to run an instance of
Linux to host the database. In your command line, cd to your vagrant file, run
the command "psql -d news -f newsdata.sql" and then run the news.py program to
get your report.

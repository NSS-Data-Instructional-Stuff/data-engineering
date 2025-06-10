## Lab 3.1

### Introduction
In last week's project you set up a postgres database. In this lab, you'll be continuing to work with this database, inserting new data and updating some records.

### Part 1
You will need to have two tables,  one you created for the api data and one created for the csv data. These tables are linked through the id column, but you'll notice that not all of the ids from the API data are present in the csv data. Use an INSERT statement to add some records to the csv table directly in the database using pgAdmin. These records should have ids that appear in the API data and which are not already present in the API table. Don't worry about adding rows for all missing ids.

### Part 2
You will also want to practice updating records, so pick a few records in the table that you made for csv data in the database and change the company to "NSS" using pgAdmin.

### Part 3
Use `INSERT ... SELECT` to create a new table by matching records from your existing two tables. This new table will mimic the output that you made into an excel file for the first project. 

### Submission
Add the SQL script that you used to complete all of the tasks above to your repo. 

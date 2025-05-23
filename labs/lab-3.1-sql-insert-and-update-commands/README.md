## Lab 3.1

### Introduction
In last week's project you set up a postgres database. In this lab, you'll be continuing to work with this database, inserting new data and updating some records.

### Part 1
You should currently have two tables, one you created for the api data and one that you created for the csv data. These tables are linked through the id column, but you'll notice that not all of the ids from the API data are present in the csv data. Use an INSERT statement to add some records to the csv table. These records should have ids that appear in the API data and which are not already present in the API table. Don't worry about adding rows for all missing ids; just add a few rows.

### Part 2
You will also want to practice updating records, so pick a few records in the table that you made for csv data and change the company to "NSS".

### Part 3
Use `INSERT ... SELECT` to create a new table by matching records from your existing two tables.
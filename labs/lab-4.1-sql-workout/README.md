## Lab 4.1

### Introduction
This lab will put your SQL skills to the test. 

### Get and examine the data
- Create a database called `nash_housing` is your local postgres database server
- Use the [property assesment backup file](https://drive.google.com/file/d/1g74eKFUEh54-ggCKmBX3A8Ei5F4mY4E4/view?usp=drive_link) to restore the `nash_housing` database
- Spend a little time exploring the tables and columns

### Create queries for each problem below
1. Open the query editor in pgAdmin and write a query to see the first 10 rows of the details table.
2.  Write a query to see what different **assessment years** are covered in the data. Record your findings as a comment after your query. 
3.  Do the same for the **last reappraisal years**. Save your query as `housing_sql_<yourLastName>.sql`. You will continue to add to this file as you complete this lab.
4. Find each unique property owner, the number of properties they own, and the total appraised value of those properties for the 12 owners who are recorded as owning the greatest number of properties. Notice that only one private citizen shows as being in the top 12 property owners. What is his name, how many properties does he own and what is the total assessed value of those properties?
5. Write a Common Table Expression (CTE) to return all information from the details table for the owner identified in the previous query. Query the CTE to understand how many of this property owner's properties are in the *General Services District (GSD)*, how many are in the *Urban Services District (USD)*, how many are *residential (RES)* and how many are commercial (COM)?
6. When did this owner acquire his properties? Look at the trend from the year he first purchased property to the year he last purchased property. What year did he buy the greatest number of properties? How many properties did he purchase?
7. Write a query which returns the year, the number of purchases, and the total acreage for years in which this owner purchased at least 5 acres.
8. `**BONUS**` Find the total land accumulated by the owner from his first year acquiring property through the final year of his acquisition.
9. Look at the sales data for each property. Write a query to return the assesor's parcel number (**apn**) and the number of times that property changed hands. Just return the properties with a sales count greater than or equal to 30.
10. Use the previous query to write a CTE. Join that CTE to the properties table to find the property address and land use description for each high sales (>= 30 sales) property _also_ join to the details table to get the tax district and assessment classification for each high sales property.
11. Investigate property purchased by foreign owners. Start by getting a count of sales for each unique owner country in the sales data.
12. Write a query to create a table of foreign purchases with 3 columns: `ownercountry`, `purchase_year`, and `purchase_count`. 

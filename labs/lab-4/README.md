## Lab 4

### Introduction
The purpose of this lab is to learn how to access data from an API using python using pagination. 

#### Part 1
Using the same API from lab 3,  go ahead and get a token, and authenticate to the API, verifying this by hitting / people. Do this in postman first. 

### Part 2
Add Query string params offset and limit to the call to get a subset of the results back.  Note here that the api is set to a max number of results of 50. Do this in postman first. 

### Part 3
Now that you have proven that the api is accessible. (This is a step I always do when writing code, so I know if it is the api that is not working vs my code not working.)

Now repeat Part 1 and 2 using Python. 

#### Part 4
Now that you can read data from the API in python, you will Save the data to a .json file 10 records at a time. Not holding any more than 10 records in memory at once. 

### Part 5 
Instead of writing this to a json file, reformat this and write to a .csv file. 
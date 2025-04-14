## Lab 5

### Introduction
The purpose of this lab is to learn how to access data from a database locally. You will be using docker to stand up a local database and a running instance of PGAdmin. 

#### Part 1
Verify that you have Docker desktop installed. 
Create a new project, put the docker-compose file in the root of the project. Open a terminal in the root of the project and run the command :  docker compose up

### Part 2
Once your containers are running. Navigate in a web browser to localhost:8080. This will pull up the login for pgadmin. You can find the local credentials in the docker compose file
In PGadmin add a server,  for host name you will use the container name postgresdb.  The database, username, password are all specified in the docker compose file. You can now manipulate your data in pgadmin. 

### Part 3 
Create a Users table with the columns: UserId, Username, LastLoginDate, CreatedDate, CreatedUserId, ModDate, ModUserId.   UserId should be the Primary key, Int, autoincrement (0,1).  
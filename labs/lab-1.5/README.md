## Lab 1.5

### Introduction
The purpose of this lab is to learn how to access data from a database locally. You will be using Docker to stand up a local database and a running instance of PGAdmin. 

#### Part 1
Verify that you have Docker desktop installed. 
Create a new project, put the docker-compose file in the root of the project. Open a terminal in the root of the project and run the command:  `docker compose up`

### Part 2
Once your containers are running. Navigate in a web browser to `localhost:8080`. This will pull up the login for **PGAdmin**. You can find the local credentials in the Docker compose file.

In PGAdmin add a server, for host name you will use the container name `postgresdb`.  The database, username, and password are all specified in the Docker compose file. You can now manipulate your data in PGAdmin. 

### Part 3 
Create a Users table with the columns: **user_id**, **username**, **last_login_date**.  **user_id** should be the primary key, with an integer data type, and set to autoincrement. 

example code: 
```  
    CREATE TABLE users (
        user_id SERIAL PRIMARY KEY,
        username varchar(40) NOT NULL,
        last_login_date date
    )
```
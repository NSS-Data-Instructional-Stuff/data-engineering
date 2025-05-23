## Lab 11.3

### Introduction
In this lab you will be turning on change data capture (CDC) in a SQL server instance. You will verify that CDC is working by making an update to the Employee table, and verifying that the SQL agent that is running has logged the difference. 

### Part 1
Install the SQL Server (mssql) extension in VSCode

### Part 2
Run the docker compose file, and verify with docker desktop that the container is running. NOTE: If you are on Mac os and have an Apple silicon chip, you will get a warning and the docker container may not start the first time, you may have to run docker compose twice. You may also need to update rosetta (softwareupdate --install-rosetta).  This lab has been verified on an M series chip, if you run into issues, the instructor can help you troubleshoot. 

### Part 3
In the SQL Server extansion, add a new connection and put in the information for the running docker container, and the password that is in the docker compose file. HINT: default username for the root account is "sa".

### Part 4
Once you are connected to the server run the sql init script. Verify that the Employee table was created and has 5 records in it. 

### Part 5 
Enable CDC at the database level. Then enable CDC at the table level. 

### Part 6
Make an update to the table (Change a name or department) 

### Part 7  
Query the changes. Here is an example of how to do that: 

```
DECLARE @from_lsn binary(10), @to_lsn binary(10);

DECLARE @name varchar(MAX) = (SELECT capture_instance
FROM cdc.change_tables
WHERE source_object_id = OBJECT_ID('dbo.Employee'))

-- Get the LSN range for the changes
SET @from_lsn = sys.fn_cdc_get_min_lsn('dbo_Employee');
SET @to_lsn = sys.fn_cdc_get_max_lsn();

-- Query the changes
SELECT *
FROM cdc.fn_cdc_get_all_changes_dbo_Employee(@from_lsn, @to_lsn, 'all')
ORDER BY __$start_lsn;
```

HINT: If you get an error that says the function fn_cdc_get_all_changes_dbo_Employee does not have enough arguments, that is due to the change not being tracked and the lsn being null. 

Here is an example of the output you should expect (yours will be in tabular form, I converted mine to json just for clarity of presentation)

```
[
  {
    "__$start_lsn": "0x0000002B000005500003",
    "__$seqval": "0x0000002B000005500002",
    "__$operation": 2,
    "__$update_mask": "0x0F",
    "EmployeeID": 6,
    "FirstName": "Alice",
    "LastName": "Green",
    "Department": "HR"
  }
]
```
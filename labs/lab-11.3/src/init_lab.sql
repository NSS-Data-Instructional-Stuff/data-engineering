/*==========================================================================
Author: Daniel Wallace
Created: 2025-05-07
Description: This is a setup script for lab 11-3, this script is idempotent and can be run multiple times without error.

==========================================================================*/

USE master
GO

--Create lab databse if not exists
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'lab11_3')
BEGIN
    CREATE DATABASE lab11_3
END
GO
USE lab11_3
GO

-- Create table if not exists
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Employee')
BEGIN
    CREATE TABLE Employee (
        EmployeeID INT PRIMARY KEY,
        FirstName NVARCHAR(50),
        LastName NVARCHAR(50),
        Department NVARCHAR(50)
    )
END
GO
-- Insert sample data if table is empty
IF NOT EXISTS (SELECT * FROM Employee)

BEGIN
    INSERT INTO Employee (EmployeeID, FirstName, LastName, Department)
    VALUES
        (1, 'John', 'Doe', 'HR'),
        (2, 'Jane', 'Smith', 'IT'),
        (3, 'Mike', 'Johnson', 'Finance'),
        (4, 'Emily', 'Davis', 'Marketing'),
        (5, 'Chris', 'Brown', 'Sales')      
END
GO

## Lab 1.1

### Introduction
The purpose of this lab is to practice fundamental python skills. You will be using pandas built-in functions to read data and send it to different outputs (csv files, console).

### Part 1
Read the `people.csv` file, and save it as `people_<yourLastName>.csv`. Verify that the data is formatted the same and no data was changed.  

### Part 2
Read the `people_no_header.csv` file, and save it as `people_header_added_<yourLastName>.csv`. Verify that the data is formatted the same and only the header was changed.

This is the header row that will need to be added:
**name,age,sex,height,weight,bmi,sibling_count,birth_order,years_played_sports**

### Part 3
Read the `people_dirty_header.csv` file, and save it as `people_clean_header_<yourLastName>.csv`. 
Verify that the data is formatted  and only the header was changed.

### Part 4
Read the `people_nulls.csv` file, and save it as `people_nulls_<yourLastName>.csv`. 
Verify that the data is formatted and nothing has changed. In this exercise, you will verify that you read in the data as a null and not as the string 'null'.  

### Part 5
Read the `people_none.csv` file, and save it as `people_none_<yourLastName>.csv`. 
Take all of the values that are 'NONE' and change them to null. Make sure it is the null object and not the string 'null'. 

### Part 6
Read in the `file people_broken.csv`
- Add the correct header
- Change any instance of NONE to null
- change any 'null' text values to null

### Part 7
Read in the `mtcars.parquet` file and print its contents to the commandline. Take a screen shot of the results.

### Part 8
Read in the `quiz.json` file and print its contents to the commandline. Take a screen shot of the results. 

### Part 9
Read in the `menu.xml` file and print its contents to the commandline. Take a screen shot of the results. 

#### Submission
Take all of the files that you created above and create a zipped folder called: `lab-1.1_<yourLastName>.zip`

#### Notes: 
Be precise when naming of your files. Code has been written to verify that the files are correct. 

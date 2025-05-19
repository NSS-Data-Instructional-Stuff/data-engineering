## Lab 1.2

### Introduction
The purpose of this lab is to practice fundamental Python skills. You will be given a custom file that you will not be able to import using pandas. 

#### Process
You will need to use Python functions to     
- open the file
- read the file line by line 
- for each line, parse the data    
- convert the data to json
- you will need to name your function ```parse_data``` it will take as input  ```input_data``` ands return a string of formatted data. 

#### Notes about the data: 

```
jobs:
-build:
--docker-image=cimg/base
--steps:
---checkout:
----run=echo "this is the build job"
-test:
--docker-image=cimg/base
--steps:
---checkout:
----run=echo "this is the test job"
```
Is Equivalent to: 
```
{
    jobs {
        build {
            docker-image: cimg/base
            steps {
                checkout {
                    run: echo 'this is the build job'
                }
            }
        }
    },
    test {
        docker-image : cimg/base:2023.03
        steps {
            checkout {
                run: echo 'this is the test job'
            }
        }
    }
} 
```

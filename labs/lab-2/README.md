## Lab 2

### Introduction
The purpose of this lab is to practice fundamental python skills. You will be given a custom file, that will not be able to be imported using pandas. 

#### Process
You will need to use python functions to open the file, read the file line by line, for each line, parse the data and convert the data to json. 

#### Notes about the data: 

jobs:build:
--docker-image=cimg/base:2023.03
--steps:checkout:
--run= echo "this is the build job"
test:
--docker-image=cimg/base:2023.03 
--steps:checkout:
--run: echo "this is the test job"

Is Equivalent to: 
{
    jobs {
        build {
            docker-image: cimg/base:2023.02
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
# Text Formatter

This Web Application accepts a POST request with the input being a JSON object containing the original text string and returns a JSON object representing a string which contains every third letter from the original string.
<br/>
<br/>


## Setup

As a prerequisite you need to have access to linux terminal and python version 3.6+ is required. Check your python version by running the following command

    python3 --version
Please also make sure that pip is installed in your system.


## Download the files

Clone the repository to your local system using the following command.

    git clone https://github.com/monishajacob/TextFormatter.git

navigate to project root by running the following command.

    cd TextFormatter

 Running `ls` should show `main.py` among other files.


## Setup the Virtual Environment

In the current folder run the following command to create a virtual environment.

    virtualenv env

Note: If virtual environment is not present please run the following command in order to install it. 

    pip3 install virtualenv

Then run the following command to change the directory to env.

    cd env

Activate the virtual environment by running the following command

    source bin/activate

After activating your virtual environment run a `ls` command to check the contents. If it does not reflect `main.py` among other files go to the previous directory by running `cd ..`
 

## Install Dependency

Install the flask dependency required by running the following command

    pip3 install requirements.txt
 

## Run the python file

In the current folder run the following command to run the python file. This will start running your flask application.

    python3 main.py


## Check the output

Open another terminal and run the following command to get the output.

    curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'


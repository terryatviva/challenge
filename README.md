# Product Reviews Application

> Product Review Application

    This Application consits of Product Reviews and also Admin panel. Most the requirements provided have been covered and additionally, Docker Files have been added for both Frontend and Backend, so it becomes easy to run the Application as mentioned in this README file. By following this README file, we can deploy it in production environment by following small changes.

## Tech Stack

- Vue.js
- Python Django framework
- PostgreSQL ([download](https://www.pgadmin.org/download/))


## Setup Development Environment

    sudo apt-get -y update
    sudo apt-get -y install git python-pip postgresql postgresql-contrib wkhtmltopdf libcurl4-openssl-dev libssl-dev xvfb
    sudo pip install virtualenv

## Clone the code

    cd ~/
    git clone git@github.com:aalluinmar/challenge.git
    cd challenge

## Install Application Requirements for Development.

- For Backend Setup, go through ([Backend README](https://github.com/aalluinmar/challenge/blob/product_reviews/backend/README.md))

- For Frontend Setup, go through ([Frontend README](https://github.com/aalluinmar/challenge/blob/product_reviews/frontend/README.md))


## Start App Server by using following Commands

- For Backend Setup, after configuring Docker Desktop in your local Environment. Open Terminal with this application path and just switch to backend directory and up the Docker Container.

    `cd backend/product_reviews/`

    `docker-compose up --build`

- For Frontend Setup, open another terminal with this application path and just switch to frontend/product_reviews_frontend directory and up the Docker Container.

    `cd frontend/product_reviews_frontend/`

    `docker-compose up --build`
    
- Open the Application using ([localhost](http://localhost:8080/))

## For Checking Backend Code Coverage and Unit Tests

- First Up the backend container and then use the following command to login into Docker Container.

- Switch to backend directory.

    `cd backend/product_reviews/`

- List the running containers using following Command.

    `docker ps`

- To login to Docker Container, use following command with the Backend Docker Container Id.

    `docker exec -it 'Container_Id' bash`

- Source the env file for running tests and checking coverage.

    `source dev.env`

- To run all Unit tests

    `coverage run manage.py test`

- To check Code Coverage and Unit Test Report.

    `coverage report -m --omit=manage.py`

## In production server, Create virtual environment and activate and Install Application Requirements regarding Backend.


    virtualenv -p python3 ~/env/productreview
    source ~/env/productreview/bin/activate
    cd backend/product_reviews/
    pip3 install -r ./requirements/test.txt

    `Configure the supervisor inorder to make Containers up every time.`

## In production server, Create virtual environment and activate and Install Application Requirements regarding Frontend.

    Install Node and Vue CLI Service and build the project for production environment setup and configure within the `S3` bucket.

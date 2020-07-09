# PRODUCT REVIEWS BACKEND

> Product Review Backend Application

## Setup Development Environment

## Update dev.env with Valid Database Credentials

    export DB_HOST=<DB_HOST>
    export DB_USERNAME=<DB_USERNAME>
    export DB_PASSWORD=<DB_PASSWORD>
    export DB_NAME=<DB_NAME>

## Setup Docker Environment

### Prerequisite

- Docker Desktop([download](https://www.docker.com/products/docker-desktop))

### Instructions

    After configuring the docker desktop, then open terminal and switch to `backend/product_reviews` directory.
    
### Migrate and load data using Docker Command

    docker-compose up --build

### List of PRODUCT REVIEWS API's

- API Docs need Basic Authentication, so we need provide basic username (admin) and password (admin@123).

    http://localhost:8000/docs/

# Contributors

Allu Aravind <alluaravind1313@gmail.com>

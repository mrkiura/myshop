# My Shop

An online shop.

This is an application that consumes [this API](http://myshop-mrkiura.herokuapp.com/docs).

You can test it out [here](https://myshop-mrkiura-fe.herokuapp.com/login/)

## API Documentation

Documentation is available [here](http://myshop-mrkiura.herokuapp.com/docs)

## Setup

Follow the steps below to get up and running

### Running the API

#### Running with docker

Ensure you are in the root directory and have docker installed on your system

run `docker-compose -f docker-compose.local.yml up -d`

The first time you run this command, the postgres image will be pulled from Docker Hub and the FastAPI application will be built from your local Dockerfile. This will take a few mins. Once it’s complete, when you run `docker ps` you should see two containers running

Now navigate to [http://localhost:8001](http://localhost:8001) and you should see the interactive REST API swagger docs. Try the following operations

* Create user
* Login
* Add a product
* Get a list of products
* Add product to cart
* Remove product from cart
* Clear cart

To stop both containers, run

```bash
docker-compose -f docker-compose.local.yml down -v
```

### Frontend

To access the frontend after running the containers, visit [http://localhost:3000](http://localhost:3000)

## Technologies used

[React](https://reactjs.org) | [FastAPI](https://fastapi.tiangolo.com)

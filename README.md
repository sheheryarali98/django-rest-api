# Django REST API

- [Django REST API](#django-rest-api)
  - [Description](#description)
  - [Prerequisites](#prerequisites)
  - [Project setup](#project-setup)
  - [Postman setup](#postman-setup)
  - [Linting](#linting)
  - [References](#references)

## Description

This project is a simple REST API implemented using **_Django_** alongwith the **_Django Rest Framework_**. **_Authentication_** is handled using **_JSON web tokens_**. It provides the following functionalities:

- Login a user and generate access and refresh tokens.
- Refresh the access token using the refresh token.
- Creating, updating and deleting users profiles.
- Creating, updating and deleting posts.

## Prerequisites

The following tools and technologies are required for the project to work properly

- [Python 3.8.9](https://www.python.org/downloads/release/python-389/)
- [PostgreSQL (14.1)](https://www.postgresql.org/)
- [Postman](https://www.postman.com/)

## Project setup

1. Clone the repo using the following command `git clone <clone_url>`
2. Navigate to the directory where the project is cloned and open terminal.
3. Run the following command to create a python virtual environment `python3 -m vevn ./env`
4. Activate the newly create virtual environment by running the following command `source ./env/bin/activate`. Make sure to run this command otherwise the packages will be intalled in the global python environment and not the newly created one for this project.
5. Run the following command to install the required packages `pip intall -r requirements.txt`
6. Create a `.env` file in the root directory and paste the following contents.

   ```
   # APPLICATION
   SECRET_KEY=<random_secret_key>

   # DATABASE
   DATABASE_ENGINE=<database_engine>
   DATABASE_NAME=<database_name>
   DATABASE_USER=<database_user>
   DATABASE_PASSWORD=<database_user_password>
   DATABASE_HOST=<database_host>
   DATABASE_PORT=<database_port>
   ```

7. Run the following commands to install the migrations `python manage.py migrate`
8. Run the following command to start the server `python manage.py runserver`

## Postman setup

To test the API endpoints a postman collection and environment is provided in the `postman` directory. Kindly follow the steps to setup the collection and environment in Postman.

1. Import the `Django REST API.postman_environment.json` file to load the environment and set that as the active environment.
2. Import the `Django REST API.postman_collection.json` file to load the collection for the available API endpoints on the server.

## Linting

For linting the code `pylint` has been used alongwith the `autopep8` guidelines. To lint the code run the following command `pylint ./*`

## References

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [JSON web tokens](https://jwt.io/)

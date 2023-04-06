# Introduction 
This API allows users to upload and retrieve images.


## Installation
* Create virtualenv ``pip install virtualenv``
* Activate virtualenv ``virtualenv venv`` (or ``python -m venv venv``)
* go into this virtualenv ``venv\Scripts\activate`` (under Linux : ``source venv/bin/activate``)
* Install dependencies : ``pip install -r requirements.txt``
* Install pre-commit for the repo : ``pre-commit install``
* Set up database : 
  * Go to source folder (``cd source``)
  * Put the file .env into source folder
  * Adapt values in .env file regarding your local database setup
  * Init database : ``flask db init``
  * Create migration : ``flask db migrate``
  * Create tables : ``flask db upgrade``


## Launch server
*  ``flask run`` (you can add ``--debug`` for check errors)


## How to use?

### User endpoint 

* /login
  * Method : POST
  * Body : {"username": "your_username", "password": "your_password"}
  * Response : {"token": "auth_token", "username": "your_username"}

* /signup
  * Method : POST
  * Body : {"username": "your_username", "password": "your_password", "first_name": "your_first_name", "last_name": "your_last_name"}
  * Response : {"token": "auth_token", "username": "your_username"}

* /logout
  * Method : POST


### Gallery

* /upload_image
  * Method : POST
  * Header : {"Authorization": "Token <token_value>"}
  * Body : {"file": "image_uploaded_by_postman_or_frontend"}
  * Response : {"message": "Image uploaded"}

* /get_images
  * Method : POST
  * Header : {"Authorization": "Token <token_value>"}
  * Response : { "images": ["image_path_1", "image_path_2", ...] }

* /get_image/<image_id>
  * Method : POST
  * Header : {"Authorization": "Token <token_value>"}
  * Response : { "image": "image_path" }
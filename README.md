# Structure Flask web application

## Overview

This application will show an approach for structuring a REST Flask web application for testing, development and production environments.

## Requirements

* Python `3.5.2`
* Python virtualenv
* `pip3`
* MongoDB

## Project Instalation and Local Testing

Install package requirements with
```
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

## Run Project

Run application with:
```
$ python manage.py runserver
```

## Project Structure

```{bash}
api
|- chat/
   |- __init__.py       
   |- api.py            /* Methods for all the routes*/
   |- conversation.py   /* All the functions for Watson Conversation API */
   |- liveperson.py     /* All the dunctions for the LivePerson API   */
   |- mongo_models.py   /* MongoDB models and functions */
   |- redis_models.py   /* Redis database model and functions */
   |- schema.py         /* Schema definition for main chat object */
   |- templates.py      /* Functions to return defined objects */
   |- views.py          /* Definition of routes using Method View Dispatching */
|- widget/
   |- __init__.py       
   |- views.py          /* Definition of routes using Method View Dispatching */
|- .env                 /* File with the credentials for local testing */
|- app.py               /* Fires up the Flask server with the configurations */
|- application.py       /* Flask API initialization */
|- config.py            /* All connections credentials and setup for IBM Cloud */
|- manage.py            /* Main file to initialize server */
|- manifest.yml         /* File for uploading the API to IBM Cloud */
|- Procfile             /* Command to run python server */
|- README.md            /* Readme file */
|- requirements.txt     /* All requirements for the application */
|- runtime.txt          /* Python version */
|- setup.py             /* Main setup config */
|- validator.py         /* Config for custom error handler */
```
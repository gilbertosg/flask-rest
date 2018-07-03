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
$ python manage.py run
```

Open the following url on your browser to view swagger documentation
http://127.0.0.1:5000/

## Project Structure

We will be using a functional structure to modularize our application. Inside the `main` package, create three more packages namely: `controller`, `service` and `model`. The `model` package will contain all of our database models while the `service` package will contain all the business logic of our application and finally the `controller` package will contain all our application endpoints. The tree structure should now look as follows:

```{bash}
.
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── controller
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── model
│   │   │   └── __init__.py
│   │   └── service
│   │       └── __init__.py
│   └── test
│       └── __init__.py
└── requirements.txt
```
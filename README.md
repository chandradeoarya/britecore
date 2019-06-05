<h1 align="center"> Britecore Flexy Insurance </h1> <br>
<p align="center">
  <a href="https://britecore.com">
    <img alt="Britecore" title="GitPoint" src="https://media.licdn.com/dms/image/C4E0BAQH0HMMwXpG7Ug/company-logo_200_200/0?e=2159024400&v=beta&t=rHvpqMtfnZLW7C1DpG8vMHntAy6n4x0tGyGb6lLcA80" width="200">
  </a>
</p>

<p align="center">
  Britecore flexy insurance for any kind of data model
</p>

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Build and Deployment](#buildanddeployment)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

#### Background
BriteCore is a web-based platform insurance companies use to manage their business. Insurance is a form of risk management. Risks are anything that someone could incur a loss on. BriteCore has historically worked primarily with property-based risks (homes, farms, churches, etc.).

#### Problem
Since BriteCore was created to work mostly with property-based insurance, the data model is pretty rigid. The data model assumes that all risks are properties and have addresses. This makes it difficult for BriteCore to work with different forms of insurance like Automobile Policies, Cyber Liability Coverage (protection against hacking), or Prize Insurance (if someone gets a $1 million hole-in-one prize at a golf tournament, the golf course doesn't pay it, they have an insurance policy to cover them).

#### Primary Goal
In a GitHub or GitLab repo, we would like to see you come up with a solution that allows insurers to define their own custom data model for their risks. There should be no database tables called automobiles, houses, or prizes. Instead, insurers should be able to create their own risk types and attach as many different fields as they would like.

Fields are bits of data like first name, age, zip code, model, serial number, Coverage A limit, or prize dollar amount. Basically any data the carrier would want to collect about the risk. Fields can also be of different types, like text, date, number, currency, and so forth.

#### Data
For the data layer, model the risk types and how the generic fields and field types would relate to these risk types. Field types must include text, number, date, or enum (where there are multiple potential options but only one choice can be made).

**Deliverables will be:**

A Python file containing the ORM classes for these tables.
An entity relationship diagram, which depicts the tables and their relationship to one another.


<p align="center">
  <img src = "https://raw.githubusercontent.com/chandradeoarya/britecore/master/screenshots/home.png" width=700>
</p>

## Features

A few of the things you can do with GitPoint:

* Handle all requests by axios
* JWT based authentication
* Redirect when token expired or not logged in
* Handle JWT with Vuex to store states
* Save states into local storage
* Integrate backend API
* API support login, create, update, delete risk
* API support CRUD functionality create, update, delete Fields
* API support types text, date, enum, number to a specific risk.
* Build and deploy script

<p align="center">
  <img src = "https://raw.githubusercontent.com/chandradeoarya/britecore/master/screenshots/dashboard.png" width=700>
</p>

<p align="center">
  <img src = "https://raw.githubusercontent.com/chandradeoarya/britecore/master/screenshots/fields.png" width=700>
</p>

<p align="center">
  <img src = "https://raw.githubusercontent.com/chandradeoarya/britecore/master/screenshots/editrisk.png" width=700>
</p>

## Setup

#### setup backend
``` sh
$ cd britecore/  
$ virtualenv  venv  

''' activate virtual env '''
$ source venv/bin/activate  

'''install dependencies'''
$ pip install -r requirements.txt  

'''create migrations'''
$ python manage.py makemigrations profiles risks  

'''migrate'''
$ python manage.py migrate  

'''create super user'''
$ python manage.py createsuperuser  

'''run development server on http://127.0.0.1:8000'''
$ python manage.py runserver  

'''unit tests'''
$ python manage.py test
```

#### setup frontend

``` sh
cd frontend

''' install dependencies '''
npm install

''' serve with hot reload at http://127.0.0.1:8080 '''
npm start

''' build for production with minification '''
npm run build
```

## Build and Deployment

The project has been built and deployed at [Britecore flexy insurance](http://ec2-18-191-84-229.us-east-2.compute.amazonaws.com).

##### Making Backend ready for deployment
* Set DEBUG= False in setting.py
* Add public address and ip in allowed hosts

#### Making Frontend ready for deployment
* Check presence of dist/ directory in frontend folder generated from build command. If not present generate it again.
* Make sure correct ROOT_API url was provided in production env file.

Now, frontend will be served by backend only.

**Deployment process on AWS EC2**  
*Process is same for any linux based instance*
``` sh
''' locate your pem file and set permission'''
$ cd path/to/your/secret/key
$ chmod 400 your_key-pair_name.pem

''' ssh into the instance '''
$ssh -i path/to/your/secret/key/your_key-pair_name.pem ubuntu@IP-ADDRESS

''' few udpates and installations '''
$ sudo apt-get update
$ sudo apt-get install nginx
$ sudo apt-get install python-pip
$ sudo pip install virtualenv
$ sudo pip install git gunicorn

'''clone the repo and follow instructions mentioned in setup and build section '''
$ git clone my-git-hub-url

'''nginx starts automatically you’ll want to shut it down'''
$ sudo service nginx stop

'''Use gunicorn for wsgi based deployment'''
$ gunicorn britecore.wsgi

'''setup nginx'''
server {

       listen 80;
       server_name ec2-18-191-84-229.us-east-2.compute.amazonaws.com 18.191.84.229;

       access_log /var/log/nginx-access.log;
       error_log /var/log/nginx-error.log;
       root /home/ubuntu/project-root;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       }
   }
   
''' restart nginx'''
$ sudo service nginx start
```
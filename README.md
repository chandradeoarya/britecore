#### Background
BriteCore is a web-based platform insurance companies use to manage their business. Insurance is a form of risk management. Risks are anything that someone could incur a loss on. BriteCore has historically worked primarily with property-based risks (homes, farms, churches, etc.).

#### Problem
Since BriteCore was created to work mostly with property-based insurance, the data model is pretty rigid. The data model assumes that all risks are properties and have addresses. This makes it difficult for BriteCore to work with different forms of insurance like Automobile Policies, Cyber Liability Coverage (protection against hacking), or Prize Insurance (if someone gets a $1 million hole-in-one prize at a golf tournament, the golf course doesn't pay it, they have an insurance policy to cover them).

#### Primary Goal
In a GitHub or GitLab repo, we would like to see you come up with a solution that allows insurers to define their own custom data model for their risks. There should be no database tables called automobiles, houses, or prizes. Instead, insurers should be able to create their own risk types and attach as many different fields as they would like.

Fields are bits of data like first name, age, zip code, model, serial number, Coverage A limit, or prize dollar amount. Basically any data the carrier would want to collect about the risk. Fields can also be of different types, like text, date, number, currency, and so forth.

#### Data
For the data layer, model the risk types and how the generic fields and field types would relate to these risk types. Field types must include text, number, date, or enum (where there are multiple potential options but only one choice can be made).

Deliverables will be:

A Python file containing the ORM classes for these tables.
An entity relationship diagram, which depicts the tables and their relationship to one another.

#### Setup

## setup backend
$ cd britecore/
$ virtualenv  venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations profiles risks
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
'''application runs at localhost:8000'''

''' To run test'''
$ python manage.py test

## setup frontend

cd my-vue-app

# install dependencies
npm install

# serve with hot reload at localhost:8080
npm start

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# To access front end
http://localhost:8080

## Development approach

* Handle all requests by axios interceptors
* JWT based authentication
* Redirect when token expired or not logged in
* Handle JWT with Vuex to store states
* Save states into local storage
* Integrate backend API
* API support login, create, update, delete Risk
* API support CRUD functionality create, update, delete Fields
* API support types text, date, enum, number to a specific risk.


For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

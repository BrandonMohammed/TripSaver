# Uber Trip Saver

#### Team Members

- Braden Messbarger
- Brandon Mohammed
- Hunter Markey
- Tristan Morris

#### Table of Contents

- [Description](#description)
- [Instructions](#instructions)
- [Known Problems](#known-problems)
- [File Submissions](#file-submissions)

---

## Description

This project is designed to help users save money when calling an Uber by determining the price of the ride if they were to walk X amount of miles from their current location. When looking for a ride the user is prompted for their destination address and how far they are willing to walk from their current address. Then the cost of the ride is determined X amount of miles in all 4 cardinal directions. Once returned, the prices of the ride from each location is then presented to the user. 

---

## Instructions

This project utilizes the following external libraries:
     - Django
     - Local Flavor
     - Geopy
     - Geocoder
     
To install all dependencies input the following command in a terminal opened in the project folder:
     - pip install -r requirements.txt
     
 ---
 
 ## Known Problems
 
 Unfortinately, we were not given access to the Uber API for getting pricing data for this project. To work around this all of the pricing data is estimated based on a price per mile and surge price that we had to compute ourselves. Each ride was given a base price of $5.00 and each mile was given a price between $1.00-$2.00. We also implemented a surge pricing between the hours of 5:00P.M. and 5:00A.M. which multiplied the price by 2.5. 
 
 ---
 
 ## File Submissions

- Trip Saver Package (All files are Django setup files)
     - __init__.py 
     - asgi.py
     - settings.py
     - urls.py
     - wsgi.py

- UberPriceCheck Package 
     - __init__.py
     - admin.py : Used for registering the models used
     - apps.py : Config for the application
     - forms.py : Used for the HTML forms for user input
     - models.py : Holds the data models for the application
     - tests.py : Unit tests for application
     - urls.py : Holds URLs for application
     - views.py : Handles the data input from the HTML form and places it into a model

- manage.py : Setup for Django
- README.MD : Readme
- requirements.txt : Contains all dependencies for project (see (#instructions))  

     


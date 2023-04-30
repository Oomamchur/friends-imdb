# Friends' IMDB Project 

Django project for managing movies and authors, 
also you can see movie ratings from other users & 
give your own evaluations for watched movies.

## Try it!

Friends' IMDB Project deployed on Render. Link:

https://friends-imdb.onrender.com/

## Installation

Python 3 should be installed

    git clone https://github.com/rakamakaphone/friends-imdb
    cd friends-imdb
    python -m venv venv
    source venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

This project uses environment variables to store sensitive information such as the Django secret key and database credentials.
Create a `.env` file in the root directory of your project and add your environment variables to it. This file should not be committed to the repository.
You can see the example in `.env.sample` file


Use the following command to load prepared data from fixture to test and debug your code:

    python manage.py loaddata fixture_data.json

After loading data from fixture you can use user (or create another one by yourself):

    Login: admin_test
    Password: !Test1234

## Features

1. Admin panel for advanced managing
2. Authentication functionality for User
3. Managing Movies and Actors on website
4. Film evaluation.

## Demo

![demo.png](demo.png)



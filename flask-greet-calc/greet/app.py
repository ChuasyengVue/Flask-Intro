from flask import Flask

app = Flask (__name__)


# Creating  a route that creates a welcome page

@app.route('/welcome')
def welcome():
    return "Welcome"


# Creating a home page that links through the welcome page

@app.route('/welcome/home')
def welcome_home(home):
    return "Welcome Home!"


# Welcome back page

@app.route('/welcome/back')
def welcome_back(back):
    return "Welcome Back!"
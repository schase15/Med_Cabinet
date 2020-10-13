# app/routes/home_routes.py

from flask import Blueprint, render_template

# Define home routes
home_routes = Blueprint("home_routes", __name__)

# Home route
@home_routes.route("/")
def index():
    '''
    Take inputs from user using drop down selections
    '''
    return render_template('recommendation_form.html')


@home_routes.route("/text_recommendation")
def text():
    '''
    Takes inputs from user using a text block
    '''

    return render_template('text_recommendation_form.html')

# app/routes/home_routes.py

from flask import Blueprint, render_template

# Define home routes
home_routes = Blueprint("home_routes", __name__)

# Home routes
@home_routes.route("/drop_down_form")
def index():
    '''
    Take inputs from user using drop down selections
    '''
    return render_template('drop_down_recommendation_form.html')


@home_routes.route("/text_recommendation")
def text():
    '''
    Takes inputs from user using a text block
    '''

    return render_template('text_recommendation_form.html')

@home_routes.route("/")
def home():
    '''
    Displays home page, gives instructions to follow nav bar links to recommendation pages
    '''

    return render_template('home_page.html')

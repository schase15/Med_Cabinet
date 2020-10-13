# This is the entry point for the web app
# Gives details on how to run program

# Import flask
from flask import Flask
import os
from dotenv import load_dotenv

# Import SQLAlchemy and Migrate objects from models page
from app.models import db, migrate

# Import routes
from app.routes.model_routes import model_routes
from app.routes.home_routes import home_routes

# Load env variables
load_dotenv()

# Set Database path 
DATABASE_URI = os.getenv('DATABASE_URI')

# For using Flash messages
SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") 

# Initialize our app
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY # For flash messages

# Configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] =DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

# Configure routes - register each route we have with the app
    app.register_blueprint(home_routes)
    app.register_blueprint(model_routes)
    return app

# Create instance of our app and return our app
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)


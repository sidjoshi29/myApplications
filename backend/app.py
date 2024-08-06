# TODO: UPDATE THIS FILE FOR DEPLOYMENT
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os


#CORS PACKAGE IS USED SO THAT SERVER CAN GET THE REQUESTS FROM THE CLIENTS WEBSITE. By default we cant send request from one server to another
# wrapping our app in CORS allows that.

app = Flask(__name__)

# We can comment this CORS config for the production because we are running the frontend and backend on the same server
# CORS(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///internships.db" #configures SQLAlchemy, the ORM (Object-Relational Mapping) tool used with Flask
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #This configuration option controls whether SQLAlchemy listens for modifications to the mapped objects and emits signals

db = SQLAlchemy(app)

# api routes
import routes

#create all tables in our database
with app.app_context():
  db.create_all()

#run the flask app
if __name__ == "__main__":
  app.run(debug=True)
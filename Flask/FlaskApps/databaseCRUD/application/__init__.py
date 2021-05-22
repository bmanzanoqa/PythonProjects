# This file will be empty in most applications

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # creates the 'app OBJECT' using the Flask class

# in-built database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

# creates the 'db OBJECT' which it is a sqlalchemy object and we pass our 'app' in there
db = SQLAlchemy(app)

from application import routes # this needs to be at the bottom because we need to create a DB before we can route anything
# all routes start with @app.route. This APP is the app object created in line 8
# if we were to import all the routes before creating the "app" it would send an error saying 'app' is not been defined (doesn't exist)
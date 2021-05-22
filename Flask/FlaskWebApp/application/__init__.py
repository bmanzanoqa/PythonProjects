from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from os import path
from flask_login import LoginManager

db = SQLAlchemy()

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

from application import templates 
from application import routes
# from .models import models

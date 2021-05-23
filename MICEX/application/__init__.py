# from app import db
from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from application import templates


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.84.151:5000/dbmicex.db"
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config["SECRET_KEY"] = "jksdhk"

db = SQLAlchemy(app)

from application import routes





# we need this to create our tables. This import the sqlalchemy object (db) created for our app
from application import db

# The SQLAlchemy object provides us with the functions and helpers we need to design our tables
# Each table is declared as a class using the declarative base db.Model.


class Games(db.Model):  # this creates the 'Games' table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

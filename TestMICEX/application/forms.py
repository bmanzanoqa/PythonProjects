from flask_wtf import FlaskForm 
from flask import url_for, redirect
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms import validators
from wtforms.validators import DataRequired, ValidationError, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.models import Exhibitions, Items


class ExhibitionsForm(FlaskForm):  
    name = StringField("Exhibition Name", validators = [DataRequired()])
    descriptions = StringField("Description")
    exhDuration = IntegerField("Duration")
    exhLocation = StringField("Location")
    exhDate = StringField("Date") 
    submit = SubmitField("Add Exhibition")


    def validate_exhname(self, name):
        allExh = Exhibitions.query.filter_by(name = Exhibitions.name).all()
        if name.data in allExh:
                raise ValidationError("That Exhibition already exists. Please choose another name")
        # return redirect(url_for('home'))

class ItemsForm(FlaskForm):  
    name = StringField("Name", validators = [DataRequired()])
    ageLevel = IntegerField("Age Level")
    difficultyLevel = IntegerField("Difficulty Level")
    numberOfPieces = IntegerField("Number Of Pieces")
    dateBuilt = StringField("Date Built") 
    photo = StringField("Photo")
    comments = StringField("Comments")
    exhid =IntegerField("Exhibition ID")
    submit = SubmitField("Add Item")

    def validate_itname(self, name):
        allit = Items.query.filter_by(name = Items.name).all()
        if name.data in allit:
                raise ValidationError("This Item already exists. Please choose another name")

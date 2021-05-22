from flask_wtf import FlaskForm  
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError


class ExhibitionsForm(FlaskForm):  
    name = StringField("Exhibition Name")
    descriptions = StringField("Description")
    exhDuration = IntegerField("Duration")
    exhLocation = StringField("Location")
    exhDate = StringField("Date") 
    submit = SubmitField("Add Exhibition")


class ItemsForm(FlaskForm):  
    name = StringField("Name")
    ageLevel = IntegerField("Age Level")
    difficultyLevel = IntegerField("Difficulty Level")
    numberOfPieces = IntegerField("Number Of Pieces")
    dateBuilt = StringField("Date Built") 
    photo = StringField("Photo")
    comments = StringField("Comments")
    exhid =IntegerField("Exhibition ID")
    submit = SubmitField("Add Item")



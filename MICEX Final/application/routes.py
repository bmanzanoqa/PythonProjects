from flask import Flask, url_for, redirect, render_template, request
from flask_table import table, Col
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Exhibitions, Items
from application import app, db
from application.forms import ExhibitionsForm, ItemsForm


@app.route('/', methods=['POST', 'GET'])
def home():
    lists = {"exhibitionsList": Exhibitions.query.all(),
    "itemsList": Items.query.all()}
    return render_template("home.html", lists=lists) 
    

# To add EXHIBITIONS
@app.route('/addex', methods=['POST', 'GET'])
def addex():
    allExh = Exhibitions.query.all()
    form = ExhibitionsForm()
    
    if request.method == "POST":
        name = form.name.data
        if not db.session.query(Exhibitions.query.filter(Exhibitions.name == name).exists()).scalar():
            newExhibition = Exhibitions(name=name)
            db.session.add(newExhibition)
            db.session.commit()
        else:
            return "That Exhibition already exists. Please choose another name"

    if form.validate_on_submit():
        newExhibition = Exhibitions(
            name=form.name.data,
            descriptions=form.descriptions.data,
            exhDuration=form.exhDuration.data,
            exhLocation=form.exhLocation.data,
            exhDate=form.exhDate.data
        )
        db.session.add(newExhibition)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('addex.html', title="Add a new Exhibition", form = form)

# To add ITEMS
@app.route('/addit', methods=['POST', 'GET'])
def addit():
    allit = Items.query.all()
    form = ItemsForm()
    
    if request.method == "POST":
        name = form.name.data
        if not db.session.query(Items.query.filter(Items.name == name).exists()).scalar():
            newItem = Items(name=name)
            db.session.add(newItem)
            db.session.commit()
        else:
            return "This Item already exists. Please choose another name"

    
    if form.validate_on_submit():
        newItem = Items(name=form.name.data, 
            ageLevel=form.ageLevel.data, 
            difficultyLevel=form.difficultyLevel.data, 
            numberOfPieces=form.numberOfPieces.data, 
            dateBuilt=form.dateBuilt.data, 
            photo=form.photo.data, 
            comments=form.comments.data, 
            exhid=form.exhid.data
        )
        db.session.add(newItem)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('addit.html', title="Add a new Item", form = form)


# To update EXHIBITIONS

@app.route("/updatex/<int:exhibitionsID>", methods=["GET", "POST"])
def updatex(exhibitionsID):  
    form = ExhibitionsForm()
    exhibitionsToUpdate = Exhibitions.query.get(exhibitionsID)
    # print(request.method)
    # print(form.validate_on_submit())
    if form.validate_on_submit():  
        exhibitionsToUpdate.name = form.name.data
        exhibitionsToUpdate.descriptions = form.descriptions.data
        exhibitionsToUpdate.exhDuration = form.exhDuration.data
        exhibitionsToUpdate.exhLocation = form.exhLocation.data
        exhibitionsToUpdate.exhDate = form.exhDate.data
        db.session.commit()
        return redirect(url_for("home"))
    elif request.method == "GET":  
        # print("hello")
        form.name.data = exhibitionsToUpdate.name
        form.descriptions.data = exhibitionsToUpdate.descriptions
        form.exhDuration.data = exhibitionsToUpdate.exhDuration
        form.exhLocation.data = exhibitionsToUpdate.exhLocation
        form.exhDate.data = exhibitionsToUpdate.exhDate
        # print(form.name.data)
    return render_template("updatex.html", title='Update your Exhibition', form=form)

# # To update  ITEMS

@app.route("/updatit/<int:itemsID>", methods=["GET", "POST"])
def updatit(itemsID):  
    form = ItemsForm()
    itemsToUpdate = Items.query.get(itemsID)
    if form.validate_on_submit():  
        itemsToUpdate.name = form.name.data
        itemsToUpdate.ageLevel = form.ageLevel.data
        itemsToUpdate.difficultyLevel = form.difficultyLevel.data
        itemsToUpdate.numberOfPieces = form.numberOfPieces.data
        itemsToUpdate.dateBuilt = form.dateBuilt.data
        itemsToUpdate.photo = form.photo.data
        itemsToUpdate.comments = form.comments.data
        itemsToUpdate.exhid = form.exhid.data
        db.session.commit()
        return redirect(url_for("home"))
    elif request.method == "GET":  
        form.name.data = itemsToUpdate.name
        form.ageLevel.data = itemsToUpdate.ageLevel
        form.difficultyLevel.data = itemsToUpdate.difficultyLevel
        form.numberOfPieces.data = itemsToUpdate.numberOfPieces
        form.dateBuilt.data = itemsToUpdate.dateBuilt
        form.photo.data = itemsToUpdate.photo
        form.comments.data = itemsToUpdate.comments
        form.exhid.data = itemsToUpdate.exhid
    return render_template("updatit.html", title='Update your Item', form=form)


# To delete EXHIBITIONS

@app.route('/deletex/<int:exhibitionsID>', methods=["GET", "POST"])
def deletex(exhibitionsID):
    exhibition = Exhibitions.query.get(exhibitionsID)
    items_with_exh=Items.query.filter_by(exhid=exhibitionsID).all()
    for item in items_with_exh:
        db.session.delete(item)
    db.session.delete(exhibition)
    db.session.commit()
    return redirect(url_for('home'))


# To delete ITEMS

@app.route('/deletit/<int:itemsID>', methods=["GET", "POST"])
def deletit(itemsID):
    item = Items.query.get(itemsID)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('home'))























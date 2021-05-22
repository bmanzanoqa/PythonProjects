from flask import Flask, url_for, redirect, render_template, request
from flask_table import table, Col
from application.models import Exhibitions, Items
from application import app, db
from application.forms import ExhibitionsForm, ItemsForm


@app.route('/', methods=['POST', 'GET'])
def home():
    lists = {"exhibitionsList": Exhibitions.query.all(),
    "itemsList": Items.query.all()}
    return render_template("home.html", lists=lists) 


headings = ("name", "Role", "Salary")
data = (
    ("Beatriz", "Carer", "10.00"),
    ("Sam", "Layer", "20.00"),
    ("Pablo", "Boxer", "5.00"),
)


@app.table("/table")
def table():
    return render_template("table.html", headings=headings, data =data)

# To add EXHIBITIONS
@app.route('/addex', methods=['POST', 'GET'])
def addex():
    form = ExhibitionsForm()
    if form.validate_on_submit():
        newExhibition = Exhibitions(name=form.name.data)
        db.session.add(newExhibition)
        db.session.commit()
        return redirect(url_for('home'))
        # return "Exhibition Added"
    return render_template('addex.html', title="Add a new Exhibition", form = form)

# To add ITEMS
@app.route('/addit', methods=['POST', 'GET'])
def addit():
    form = ItemsForm()
    if form.validate_on_submit():
        newItem = Items(name=form.name.data)
        db.session.add(newItem)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('addit.html', title="Add a new Item", form = form)


# To update EXHIBITIONS

@app.route("/updatex/<int:id>", methods=["GET", "POST"])
def updatex(exhibitionsID):  
    form = ExhibitionsForm()
    exhibitionsToUpdate = Exhibitions.query.get(exhibitionsID)
    if form.validate_on_submit():  
        exhibitionsToUpdate.name = form.name.data
        db.session.commit()
        return redirect(url_for("home"))
    elif request.method == "GET":  
        form.name.data = exhibitionsToUpdate.name
    return render_template("updatex.html", title='Update your Exhibition', form=form)

# # To update  ITEMS

@app.route("/updatit/<int:id>", methods=["GET", "POST"])
def updatit(itemsID):  
    form = ItemsForm()
    itemsToUpdate = Items.query.get(itemsID)
    if form.validate_on_submit():  
        itemsToUpdate.name = form.name.data
        db.session.commit()
        return redirect(url_for("home"))
    elif request.method == "GET":  
        form.name.data = itemsToUpdate.name
    return render_template("updatit.html", title='Update your Item', form=form)


# To delete EXHIBITIONS

@app.route('/deletex/<int:id>', methods=["GET", "POST"])
def deletex(exhibitionsID):
    exhibition = Exhibitions.query.get(exhibitionsID)
    db.session.delete(exhibition)
    db.session.commit()
    return redirect(url_for('home'))


# To delete ITEMS

@app.route('/deletit/<int:id>', methods=["GET", "POST"])
def deletit(itemsID):
    item = Items.query.get(itemsID)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('home'))























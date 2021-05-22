from application import db


class Items(db.Model):
    itemsID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    ageLevel = db.column(db.Integer, nullable=True)
    difficultyLevel = db.column(db.Integer, nullable=True)
    numberOfPieces = db.column(db.Integer, nullable=True)
    dateBuilt = db.column(db.Date, nullable=True)
    photo = db.Column(db.String(100), unique=True, nullable=True)
    comments = db.Column(db.String(150), nullable=True)
    complete = db.Column(db.Boolean, default=False)


class Exhibitions(db.Model):
    exhibitionsID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    descriptions = db.Column(db.String(150), nullable=True)
    exhDate: db.column(db.Date, nullable=True)
    exhDuration = db.column(db.Integer, nullable=True)
    exhLocation = db.column(db.String(20), nullable=True)

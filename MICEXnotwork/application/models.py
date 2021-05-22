from application import db


class Exhibitions(db.Model):
    exhibitionsID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    descriptions = db.Column(db.String(150), nullable=True)
    exhDuration = db.Column(db.Integer, nullable=True)
    exhLocation = db.Column(db.String(20), nullable=True)
    exhDate = db.Column(db.String(20), nullable=True)
    itexh = db.relationship('Items', backref='builds')


class Items(db.Model):
    itemsID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ageLevel = db.Column(db.Integer, nullable=True)
    difficultyLevel = db.Column(db.Integer, nullable=True)
    numberOfPieces = db.Column(db.Integer, nullable=True)
    dateBuilt = db.Column(db.String(20), nullable=True)
    photo = db.Column(db.String(100), nullable=True)
    comments = db.Column(db.String(150), nullable=True)
    # complete = db.Column(db.Boolean, default=False)
    exhid = db.Column(db.Integer, db.ForeignKey(
        'exhibitions.exhibitionsID'), nullable=False)




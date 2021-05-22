from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 

class Exhibitions(db.Model):
    exhibitionsID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    descriptions = db.Column(db.String(150), nullable=True)
    exhDuration = db.Column(db.Integer, nullable=True)
    exhLocation = db.Column(db.String(20), nullable=True)
    exhDate = db.Column(db.Date, nullable=True)
    itexh = db.relationship('Items', backref='builds')


class Items(db.Model):
    itemsID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    ageLevel = db.Column(db.Integer, nullable=True)
    difficultyLevel = db.Column(db.Integer, nullable=True)
    numberOfPieces = db.Column(db.Integer, nullable=True)
    dateBuilt = db.Column(db.DateTime(), nullable=True)
    photo = db.Column(db.String(100), unique=True, nullable=True)
    comments = db.Column(db.String(150), nullable=True)
    complete = db.Column(db.Boolean, default=False)
    exhid = db.Column(db.Integer, db.ForeignKey(
        'exhibitions.exhibitionsID'), nullable=False)


db.create_all()
newExhibition = Exhibitions(
    name="Buildings & Wonders",
    descriptions="Some skylines & wonders of the world",
    exhDuration=14,
    exhLocation="London",
    exhDate="2021-05-25"
)

newItem = Items(
    name="Big Ben",
    ageLevel=14,
    difficultyLevel=4,
    numberOfPieces=3600,
    dateBuilt="2019-01-1",
    photo=True,
    comments="My first building!",
    exhid=1
)



# class EmployeeModel(db.Model):
#     __tablename__ = "table"
 
#     id = db.Column(db.Integer, primary_key=True)
#     employee_id = db.Column(db.Integer(),unique = True)
#     name = db.Column(db.String())
#     age = db.Column(db.Integer())
#     position = db.Column(db.String(80))
 
#     def __init__(self, employee_id,name,age,position):
#         self.employee_id = employee_id
#         self.name = name
#         self.age = age
#         self.position = position
 
#     def __repr__(self):
#         return f"{self.name}:{self.employee_id}"

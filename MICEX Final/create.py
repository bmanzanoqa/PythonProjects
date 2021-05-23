from application import db
from application.models import Exhibitions, Items

print("Opening Microblocks Exhibitions ....")

print("Deleting any previous databases, please wait .....")
db.drop_all()

print("Creating a new database")
db.create_all()

#Some data samples

newExhibition = Exhibitions(
    name="Buildings & Wonders",
    descriptions="Some skylines & wonders of the world",
    exhDuration=14,
    exhLocation="London",
    exhDate="25-05-2021")

newExhibition1 = Exhibitions(
    name="Animal Kingdom",
    descriptions="Our best friends",
    exhDuration=7,
    exhLocation="Madrid",
    exhDate="12-11-2021")

newItem = Items(
    name="Big Ben",
    ageLevel=14,
    difficultyLevel=4,
    numberOfPieces=3600,
    dateBuilt="2019-01-1",
    photo=True,
    comments="My first building!",
    exhid=1)

newItem1 = Items(
    name="Statute of Liberty",
    ageLevel=14,
    difficultyLevel=4,
    numberOfPieces=2510,
    dateBuilt="2019-05-20",
    photo=True,
    comments="This one is beautiful!",
    exhid=1)

newItem2 = Items(
    name="Welsh Sheepdog",
    ageLevel=6,
    difficultyLevel=3,
    numberOfPieces=1962,
    dateBuilt="2021-04-17",
    photo=True,
    comments="This is for my son's birthaday on thde 25/5/2021",
    exhid=2)


db.session.add(newExhibition)
db.session.add(newExhibition1)
db.session.add(newItem)
db.session.add(newItem1)
db.session.add(newItem2)
db.session.commit()


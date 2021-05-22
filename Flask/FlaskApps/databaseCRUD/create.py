# This will mostly be the same in most applications

from application import db

db.drop_all()
db.create_all()

# we import the SQLAlchemy object db and the Users class defined in app.py so we can add data to our USERS' Table
from app import db, Users

# The two functions db.drop_all() and db.create_all() delete all tables then create all tables defined for our db object.
db.drop_all()
db.create_all()

# Extra: this section populates the table with an example entry
user1 = Users(first_name='Ben', last_name='Toot')
db.session.add(user1)
db.session.commit()

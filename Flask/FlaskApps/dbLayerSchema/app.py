from flask import Flask  # Import Flask class
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy class

app = Flask(__name__)  # create Flask object

# Set the connection string to connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.105.152.18/myflaskdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # create SQLALchemy object

# THIS IS OUR TABLE


class Users(db.Model):  # the Users' table inherits the 'Model' Table from db
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

# Now in 'create.py' we can add some data to our Users' Table (see create.py lines 9-11 )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

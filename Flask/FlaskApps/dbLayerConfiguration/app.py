# Database Layer Configuration for IN-BUILD DB
'''
1. We need to install and import the SQLAlchemy class to associate our database layer with our app.
2. Once our URI configuration has been set, as above, we can create a db object. 
3. This DB OBJECT will hold all of our data for when we need it.
        from flask_sqlalchemy import SQLAlchemy  
        db = SQLAlchemy(app)  ==>> we pass our app object into the SQLA class so the DB OBJECT knows the db we are using will work with 
                                    this app object

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)

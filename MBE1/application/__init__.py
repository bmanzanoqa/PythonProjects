from application import routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/miniblocksexhibitions"

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
# app.config['SECRET_KEY'] = "uiwyetskug"

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

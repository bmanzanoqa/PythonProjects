# from flask module we import the class Flask and all its functions
from flask import Flask

app = Flask(__name__)


# this is a DECORATOR. It always comes with a function defined below
@app.route('/')
@app.route('/home')  # this 2 statements do the same thing
def home():
    return "This is the home page"


@app.route('/about')
def about():
    return "This is the ABOUT page"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

# FLASK ==>> creates very simple apps written in just a few lines of code as well as complex
# enterprise-level applications.

# imports the Flask module, which instantiates the Flask app.
from flask import Flask

app = Flask(__name__)  # where the app object is created.


@app.route('/')  # This is the app's function
def hello_internet():
    return "Hello Internet!"


if __name__ == '__main__':  # allows us to run the app by running app.py from the command line
    app.run(debug=True, host='0.0.0.0')

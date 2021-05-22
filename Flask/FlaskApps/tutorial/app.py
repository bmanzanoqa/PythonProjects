# set up the app object
from flask import Flask, render_template
from flask_wtf import FlaskForm
# We will only use StringField and SubmitField in myForm.
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
# Configure a secret key for CSRF protection.
app.config['SECRET_KEY'] = 'djkshkfudkhglskj'

# create a validator (CUSTOM VALIDATOR)


class UserCheck:
    # Here we set up the class to have the banned and message attributes. banned must be passed through at declaration.
    def __init__(self, banned, message=None):
        self.banned = banned
        if not message:
            # If no message chosen, then this default message is returned.
            message = 'Please choose another username'
        self.message = message

    def __call__(self, form, field):
        # Here we define the method that is ran when the class is called. If the data in our field is in the list of words then raise a ValidationError object with a message.
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)


''' 1. create a form consisting of a StringField labelled Username
    2. add the validators DataRequired, Length, and our custom one UserCheck. 
    3. create a button with SubmitField '''


class myForm(FlaskForm):  # inherit Frlask form
    username = StringField('Username', validators=[  # validators are a list
        DataRequired(),
        # We call our custom validator here, and pass through a message to override the default one. We pass through the list of banned usernames as a list.
        UserCheck(
            message="custom rejection message",
            banned=['root', 'admin', 'sys']),
        Length(min=2, max=15)
    ])
    submit = SubmitField('Sign up')

# ROUTE ==>> it defines the behavior of our app


@app.route('/', methods=['GET', 'POST'])
def postName():
    form = myForm()  # creates the instance of our for
    if form.validate_on_submit():  # validates our form
        username = form.username.data
        return render_template('home.html', form=form, username=username)
    else:
        return render_template('home.html', form=form, username="")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

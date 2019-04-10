from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class SignUpForm(FlaskForm):
    firstName = StringField('First Name', validators=[InputRequired()])
    lastName = StringField('Last Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    ccNum = StringField('Card Number', validators=[InputRequired()]) # Number data type
    ccType = StringField('Credit Card Type', validators=[InputRequired()])
    CCV = StringField('Card CCV', validators=[InputRequired()]) # Number Data type
    expDate = StringField('Card Expiry Date', validators=[InputRequired()]) # Date data type
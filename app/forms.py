"""Form definitions used by Flask-WTF throughout the project."""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    """Form for authenticating existing users."""

    # Required username field
    username = StringField('Username', validators=[DataRequired()])
    # Password field is also required
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    """Form used to create a new user account."""

    username = StringField('Username', validators=[DataRequired()])
    # Password must be confirmed by the user
    password = PasswordField(
        'Password',
        validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')]
    )
    confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class ContactForm(FlaskForm):
    """Form for users to send contact messages."""

    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    # Limit length of the message field
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Send')

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(message="Name is required."),
        Length(max=100, message="Name must be 100 characters or less.")
    ])
    phone = StringField('Phone', validators=[
        DataRequired(message="Phone number is required."),
        Length(min=10, max=15, message="Phone number must be between 10 and 15 digits."),
        Regexp(r'^[0-9]+$', message="Phone number must contain only digits.")
    ])
    email = StringField('Email', validators=[
        Email(message="Invalid email address."),
        Length(max=100, message="Email must be 100 characters or less.")
    ])
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                               ('Work', 'Work'), 
                               ('Other', 'Other')],
                      validators=[DataRequired(message="Please select a contact type.")])
    submit = SubmitField('Submit')

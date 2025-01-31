from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                               ('Work', 'Work'), 
                               ('Other', 'Other')],
                      validators=[DataRequired()])
    submit = SubmitField('Submit')


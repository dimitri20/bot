from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

class CommandForm(FlaskForm):
    search = StringField('')
    submit = SubmitField('')

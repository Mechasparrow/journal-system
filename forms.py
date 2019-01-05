# forms
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, TextAreaField, StringField, validators

class PostForm(FlaskForm):
    title = StringField('Title', validators = [validators.DataRequired()])
    content = TextAreaField('Content', validators = [validators.DataRequired()])

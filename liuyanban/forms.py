from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime


class TipForm(FlaskForm):
    poster = StringField("Poster Name",validators=[DataRequired()])
    body = TextAreaField("Tip Content",validators=[DataRequired()])
    posttime = DateTimeField("Post Time",default=datetime.now)
    submit = SubmitField("Post")
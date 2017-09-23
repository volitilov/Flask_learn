from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import Required


class TestForm(FlaskForm):
	name = TextField('name', validators=[Required()])
	submit = SubmitField('submit')
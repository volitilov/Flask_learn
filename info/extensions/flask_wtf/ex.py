#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required, Email

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class NameForm(FlaskForm):
	email = TextField('text field', validators=[Required(), Email()])

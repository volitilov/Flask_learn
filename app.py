import os

# flask
from flask import (
	Flask, url_for, render_template, session,
	request, make_response, redirect, flash
)

# flask_script
from flask_script import Manager

# flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired

# flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
			'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class MyForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	text = TextAreaField('text', validators=[DataRequired()])



@app.route('/', methods=('GET', 'POST'))
def index():
	name, password, text = None, None, None
	form = MyForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('This name: {} - new'.format(form.name.data))
		session['name'] = form.name.data
		form.name.data = '' 
		return redirect(url_for('index'))

	return render_template('index.html', 
						form=form, 
						name=session.get('name'))



# errors :::::::::::::::::::::::::::::::::::::::::::::
@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
	return render_template('500.html'), 500
# end errors :::::::::::::::::::::::::::::::::::::::::


manager = Manager(app)

if __name__ == '__main__':
	app.debug = True
	manager.run()
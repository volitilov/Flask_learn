from app import app
from flask import render_template

@app.route('/user/<name>')
def user(name):
 return 'Hello {}'.format(name)

from flask import Flask, make_response, redirect, request

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

app = Flask(__name__)

@app.route('/')
def home():
	name = request.cookies.get('user')
	return '<h3>Hello {}</h3>'.format(name)


@app.route('/<name>')
def user(name):
	response = make_response('<h2>Hello {}</h2>'.format(name))
	response.set_cookie('user', name)
	return response

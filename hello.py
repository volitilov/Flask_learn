from flask import Flask
# from flask import request
# from flask import make_response
# from flask import redirect
# from flask import abort
# from flask.ext.script import Manager 

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

app = Flask(__name__)
# manager = Manager(app)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# @app.route('/')
# def index():
# 	user_agent = request.headers.get('User-agent')
#     return '<p>Your browser is {}</p>'.format(user_agent)


# @app.route('/')
# def index():
# 	response = make_response('<h3>This document carries cookie</h3>')
# 	response.set_cookie('answer', '42')
# 	return response


# @app.route('/')
# def index():
# 	return redirect('https://www.example.com')


# @app.route('/user/<id>')
# def get_user(id):
# 	user = load_user(id)
# 	if not user:
# 		abort(404)
# 	else:
# 		return '<h3>Hay {}</h3>'.format(user.name)


# ...


@app.route('/')
def index():
	return '<h3>Hay</h3>', 400


@app.route('/user/<username>')
def user(username):
    return '<h1>Hay {}</h1>'.format(username)


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	app.run(debug=True)
	# manager.run(debug=True)
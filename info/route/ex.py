from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index(): pass


@app.route('/login')
def login(): pass


@app.route('/user/<user_name>')
def profile(user_name): pass



if __name__ == '__main__':
	with app.test_request_context():
		print(url_for('index')) 							# /
		print(url_for('login')) 							# /login
		print(url_for('login', next='/')) 					# /login?next=%2F
		print(url_for('profile', user_name='Sam Dokins')) 	# /user/Sam%20Dokins
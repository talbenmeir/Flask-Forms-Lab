from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "tal"
password = "123"
facebook_friends=["Roei","Roni","Geffen", "Ella","Lia", "Mia", "Not Niv"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username1 = request.form['username']
		password1 = request.form['password']
		if password1==password and username1==username:
			return redirect(url_for('home'))
	return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', friend=facebook_friends)

@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])
def friends(name):
	flag = False
	if name in facebook_friends:
		flag = True
	return render_template('friend_exists.html', name=name, flag = flag)
  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
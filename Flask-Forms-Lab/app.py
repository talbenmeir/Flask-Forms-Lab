from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "tal"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username1 = request.form['username']
		password1 = request.form['password']
		if password1==password and username1==username:
			return render_template('home.html')
			return render_template('login.html')
  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
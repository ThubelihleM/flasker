from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)


"""
1. FILTERS

safe
capitalize
lower
upper
title
trim
scripttags
"""

# Create a route decorator
@app.route('/')
def index():
	user_name = "Thube"
	stuff = "This is bold bext"

	favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
	return render_template('index.html', 
		name=user_name,
		stuff=stuff,
		favorite_pizza = favorite_pizza)

# http://localhost:5000/user/Thube
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', user_name=name)

# Create customer error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500

if __name__ == "__main__":
	app.run(debug=True)

from flask import Flask, render_template

my_app = Flask(__name__)

myskills = [
    ("Python", 5),
    ("JavaScript", 4),
    ("HTML/CSS", 4),
    ("Flask", 5),
    ("Django", 4)
]

@my_app.route('/')
def home():
    return render_template('index.html', title="Home", custom_css = 'home')

@my_app.route('/add')
def add():
    return render_template('add.html', title="Add", custom_css = 'add')

@my_app.route('/about')
def about():
    return render_template('about.html', title="About")

@my_app.route('/skills')
def skills():
    return render_template('skills.html',
                            title="Skills",
                            heading="My Skills",
                            skills_list = myskills)

if __name__ == "__main__":
    my_app.run(debug=True, port=10000)
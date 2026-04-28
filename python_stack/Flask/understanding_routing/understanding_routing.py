
from flask import Flask

app = Flask(__name__)

# 1-  say "Hello World!" - localhost:5000/ 
@app.route('/')
def hello():
    return 'Hello, World!'

# 2- say "Champion!" - localhost:5000/champion
@app.route('/champion')
def champion():
    return 'Champion!'

# 3- say "Hi [Name]!" - localhost:5000/say/[name]
@app.route('/say/<name>')
def say_hi(name):
    return f"Hi {name.capitalize()}!"

# 4- repeat a string [num] times - localhost:5000/repeat/[num]/[word]
@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return (word + "  ") * num

# 5- handle 404 errors with a custom message
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404


if __name__ == '__main__':
    app.run(debug=True)
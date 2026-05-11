from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():

    print(request.form)
    
    name = request.form['name']
    location = request.form['location']
    level = request.form['level']
    languages = request.form.getlist('languages[]')
    comment = request.form['comment']
    
    return render_template('result.html', 
                            name=name, 
                            location=location, 
                            level=level, 
                            languages=languages, 
                            comment=comment)


if __name__ == '__main__':
    app.run(debug=True)
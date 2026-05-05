from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    # print data received from the form for debugging purposes
    print(request.form)
    
    # get data from the form
    name = request.form['name']
    location = request.form['location']
    level = request.form['level']
    languages = request.form.getlist('languages[]')
    comment = request.form['comment']
    
    # render the result template with the data received from the form
    return render_template('result.html', 
                            name=name, 
                            location=location, 
                            level=level, 
                            languages=languages, 
                            comment=comment)

if __name__ == '__main__':
    app.run(debug=True)
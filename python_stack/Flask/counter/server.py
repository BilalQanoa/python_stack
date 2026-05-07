from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'your_super_secret_key_here' 

@app.route('/')
def index():

    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 0

    if 'count' not in session:
        session['count'] = 1
    
        
    return render_template("index.html")

@app.route('/add_two')
def add_two():

    session['count'] += 1
    session['visits'] -= 1
    return redirect('/')

@app.route('/reset')
def reset_count():
    session['count'] = 0 
    return redirect('/')

@app.route('/custom_increment', methods=['POST'])
def custom_increment():

    inc_value = request.form.get('increment')
    if inc_value and inc_value.isdigit():

        session['count'] += int(inc_value) - 1
        session['visits'] -= 1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    if 'visits' in session:
        session.pop('visits')
    # session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
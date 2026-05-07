from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'ninja_secret_gold_key'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
        session['moves'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    
    buildings = {
        'farm': (10, 20),
        'cave': (5, 10),
        'house': (2, 5),
        'casino': (-50, 50)
    }

    building = request.form['building']
    if building in buildings:

        gold_range = buildings[building]
        earned = random.randint(gold_range[0], gold_range[1])
        
        session['gold'] += earned
        session['moves'] += 1
        
        now = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        
        if earned >= 0:
            msg = f"Earned {earned} golds from the {building}! ({now})"
            color = "text-success"
        else:
            msg = f"Entered a casino and lost {abs(earned)} golds... Ouch. ({now})"
            color = "text-danger"
            
        new_activity = {'message': msg, 'color': color}
        session['activities'].insert(0, new_activity)
        session.modified = True

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
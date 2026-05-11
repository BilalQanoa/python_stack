from flask import Flask, render_template, request, redirect, session
import random
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

LEADERBOARD_FILE = 'leaderboard.json'

def init_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, 'w') as f:
            json.dump([], f)

def get_leaderboard():
    init_leaderboard()
    with open(LEADERBOARD_FILE, 'r') as f:
        return json.load(f)

def add_to_leaderboard(name, attempts):
    scores = get_leaderboard()
    scores.append({'name': name, 'attempts': attempts})
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(scores, f)

@app.route('/')
def index():
    if 'target_num' not in session:
        session['target_num'] = random.randint(1, 100)
        session['attempts'] = 0
        session['status'] = None
        session['last_guess'] = None
    
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if 'target_num' not in session:
        return redirect('/')

    user_guess = int(request.form['guess'])
    session['attempts'] += 1
    session['last_guess'] = user_guess
    
    target = session['target_num']
    attempts = session['attempts']
    
    if user_guess == target:
        session['status'] = 'correct'
    elif user_guess < target:
        session['status'] = 'too_low'
    else:
        session['status'] = 'too_high'
    
    if session['status'] != 'correct' and attempts >= 5:
        session['status'] = 'lose'
        
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/submit_score', methods=['POST'])
def submit_score():
    name = request.form.get('name', 'Anonymous')
    attempts = session.get('attempts', 0)
    if session.get('status') == 'correct':
        add_to_leaderboard(name, attempts)
    return redirect('/leaderboard')

@app.route('/leaderboard')
def leaderboard():
    scores = get_leaderboard()
    return render_template('leaderboard.html', scores=scores)


if __name__ == '__main__':
    app.run(debug=True)
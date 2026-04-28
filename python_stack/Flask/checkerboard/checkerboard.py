from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', col=8, row=8)

@app.route('/<int:row>')
def play_row(row):
    return render_template('home.html', col=8, row=row)

@app.route('/<int:col>/<int:row>')
def play_col_row(col, row):
    return render_template('home.html', col=col, row=row)

if __name__ == '__main__':
    app.run(debug=True)
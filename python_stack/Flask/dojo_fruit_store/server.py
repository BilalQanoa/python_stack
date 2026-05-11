from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__) 
app.secret_key = 'HereIsASecretKeyForDojoFruitStore' 

@app.route('/')          
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    order = {
        'strawberry': int(request.form.get('strawberry', 0)),
        'raspberry': int(request.form.get('raspberry', 0)),
        'apple': int(request.form.get('apple', 0)),
        'blackberry': int(request.form.get('blackberry', 0))
    }
    
    session['customer_name'] = f"{request.form.get('first_name', '')} {request.form.get('last_name', '')}".strip()
    session['total_fruits'] = sum(order.values())
    session['order_time'] = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    session['order'] = order
    session['student_id'] = request.form.get('student_id', '')

    print(f"Charging {session['customer_name']} for {session['total_fruits']} fruits.")

    return redirect('/success') 

@app.route('/success')
def success():
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)
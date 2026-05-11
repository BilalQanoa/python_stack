from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__) 

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
    
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    student_id = request.form.get('student_id', '')
    
    total_fruits = sum(order.values())
    customer_name = f"{first_name} {last_name}".strip()
    
    print(f"Charging {customer_name} for {total_fruits} fruits.")
    
    now = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    
    return render_template("checkout.html", 
                            order=order,
                            total_fruits=total_fruits,
                            first_name=first_name,
                            last_name=last_name,
                            student_id=student_id,
                            order_time=now)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)
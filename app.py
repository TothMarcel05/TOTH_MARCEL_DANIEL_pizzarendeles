from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

orders = []
@app.route('/order-summary', methods=["GET"])
def order_summary():
    return render_template('order_summary.html')

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/pizza-order', methods=["GET", "POST"])
def pizza_order():
    if request.method == 'POST':
        _name = request.form.get('name')
        _phone = request.form.get('phone')
        _size = request.form.get('size')
        _ham = request.form.get('ham')
        _cheese = request.form.get('cheese')
        _mushroom = request.form.get('mushroom')
        _measure = request.form.get('measure')
        _time = request.form.get('time')
        _more = request.form.get('more')
        order ={
            'name': _name,
            'phone': _phone,
            'size': _size,
            'ham': _ham,
            'cheese': _cheese,
            'mushroom': _mushroom,
            'measure': _measure,
            'time': _time,
            'more': _more}
        orders.append(order)
        print(orders)
    return render_template('pizza_order.html')
    

if __name__ == "__main__":
    app.run(debug=True)

        
       


 
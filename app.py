from flask import Flask, render_template, jsonify, abort, request
from database import load_orders_from_db, load_order_from_db

app = Flask(__name__)

@app.route("/")
def hello():
  orders = load_orders_from_db()
  return render_template('home.html',
                         orders=orders)

@app.route("/orders/<int:id>")
def show_order(id):
    order = load_order_from_db(id)
    if order is None:
        abort(404)  # Order not found, return 404 status
    return render_template('orderpage.html', order=order)

@app.route("/orders")
def list_of_orders():
   orders = load_orders_from_db()
   return render_template('orders.html',
                          orders=orders)

@app.route("/new-order")
def new_order():
   return render_template('create_new_order.html')

@app.route("/order/<int:id>/submit", methods=["GET"])
def submit_order(id):
    data = request.args.to_dict()
    return jsonify(data)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8080)
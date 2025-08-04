from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# In-memory storage for demo purposes
ORDERS = []

# Logging configuration
logging.basicConfig(
    filename='order.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    user = data.get("user")
    product = data.get("product")

    if not user or not product:
        logging.warning("Order failed: Missing user or product")
        return jsonify({"error": "Missing user or product"}), 400

    order = {"user": user, "product": product}
    ORDERS.append(order)

    logging.info(f"New order: {order}")
    return jsonify({
        "message": f"Order confirmed for {user}",
        "order": order
    }), 201

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(ORDERS), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
import razorpay
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Razorpay client instance
razorpay_client = razorpay.Client(
    auth=(os.getenv("RAZORPAY_KEY_ID"), os.getenv("RAZORPAY_KEY_SECRET"))
)

# In-memory order database (for testing only)
orders_db = []

@app.route("/", methods=["GET"])
def home():
    return "✅ Flask Razorpay API is running!"

@app.route("/create-order", methods=["POST"])
def create_order():
    try:
        data = request.json
        print("Request Body:", data)

        amount = int(data["price"]) * 100  # Convert to paise
        currency = "INR"
        options = {
            "amount": amount,
            "currency": currency,
            "payment_capture": '1'
        }

        order = razorpay_client.order.create(options)

        if not order:
            return jsonify({"message": "Some error occurred"}), 500

        return jsonify(order), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/pay-order", methods=["POST"])
def pay_order():
    try:
        data = request.json
        print("Payment Data:", data)

        new_order = {
            "isPaid": True,
            "amount": data["amount"],
            "razorpay": {
                "order_id": data["razorpayOrderId"],
                "payment_id": data["razorpayPaymentId"],
                "signature": data["razorpaySignature"]
            }
        }

        # Store the payment (mock DB)
        orders_db.append(new_order)

        return jsonify({"msg": "Payment was successful", "order": new_order}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/payment-response", methods=["GET"])
def payment_response():
    try:
        print("All Orders:", orders_db)
        return jsonify(orders_db), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

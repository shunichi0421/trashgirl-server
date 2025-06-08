import os
import requests
import uuid

def create_komoju_payment():
    KOMOJU_SECRET_KEY = os.environ["KOMOJU_SECRET_KEY"]
    order_id = str(uuid.uuid4())

    response = requests.post(
        "https://sandbox.komoju.com/api/v1/payments",
        auth=(KOMOJU_SECRET_KEY, ""),
        json={
            "amount": 300,
            "currency": "JPY",
            "merchant_order_id": order_id,
            "return_url": f"https://yourdomain.com/post-payment.html?komoju_id={order_id}",
            "payment_method_types": ["credit_card"]
        }
    ).json()

    return order_id, response["redirect_url"]

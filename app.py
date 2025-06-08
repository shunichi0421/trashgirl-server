from flask import Flask, request, redirect
from komoju_utils import create_komoju_payment
from firestore_utils import save_token_for_order_id, mark_order_as_used

app = Flask(__name__)

@app.route("/")
def hello():
    return "Trash Girl KOMOJU Webhook Server is running!"

@app.route("/create-komoju-session", methods=["POST"])
def create_session():
    # KOMOJUセッションを作成し、リダイレクトURLを取得
    order_id, redirect_url = create_komoju_payment()
    
    # Firestoreに order_id と unusedトークンを保存
    save_token_for_order_id(order_id)
    
    # 購入画面へリダイレクト
    return redirect(redirect_url)

@app.route("/webhook", methods=["POST"])
def komoju_webhook():
    data = request.json

    # 支払い完了イベントのみ処理
    if data and data.get("event") == "payment.paid":
        order_id = data["data"]["attributes"]["merchant_order_id"]
        
        # Firestore上のトークンに "used": true をマーク
        mark_order_as_used(order_id)

    return "", 200

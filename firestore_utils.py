import os
import firebase_admin
from firebase_admin import credentials, firestore

# Firebaseアプリの初期化（既に初期化されていない場合のみ）
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-service-account.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

def save_token_for_order_id(order_id):
    doc_ref = db.collection("tokens").document(order_id)
    doc_ref.set({
        "used": False,
        "createdAt": firestore.SERVER_TIMESTAMP
    })

def mark_order_as_used(order_id):
    doc_ref = db.collection("tokens").document(order_id)
    doc_ref.update({
        "used": True
    })

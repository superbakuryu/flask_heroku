from flask import Flask
from datetime import datetime

app = Flask(__name__)

DB_FAKE = []

@app.route("/")
def hello():
    NOW = datetime.now().timestamp()
    DB_FAKE.append({'created_at': NOW})
    num = len(DB_FAKE)
    return f"Số lượt truy cập: {num}"
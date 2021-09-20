from flask import Flask
import pymongo
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://mongo/")
mydb = myclient["mydatabase"]
app = Flask(__name__)

@app.route("/")
def hello():
    NOW = datetime.now().timestamp()
    mydb.visits.insert_one({'created_at': NOW})
    num = mydb.visits.count_documents({})
    return f"Số lượt truy cập: {num}"
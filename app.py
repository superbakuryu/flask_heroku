from flask import Flask
from datetime import datetime
import pymongo
app = Flask(__name__)

myclient = pymongo.MongoClient('mongodb+srv://thuan:thuan@cluster0.9gguq.mongodb.net/test')
mydb = myclient["mydatabase"]

@app.route("/")
def hello():
    NOW = datetime.now()
    mydb.visits.insert_one({'created_at': NOW})
    num = mydb.visits.count_documents({})
    return f"Số lượt truy cập: {num}"
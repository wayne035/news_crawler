from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("DB"))
news_db = client.db

def find_all_data(page):
    find_data = news_db["news"].find({},{"_id": False}).skip(page * 50).limit(50)
    return list(find_data)

def find_other_data(news_name):
    find_data = news_db["news"].find({'en':news_name},{"_id": False})
    return list(find_data)

def insert_mary_data(data):
    news_db["news"].insert_many(data)
    print('儲存成功')

def delete_document():
    news_db["news"].delete_many({})
    print('資料已全部刪除')
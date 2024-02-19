from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("DB"))
db = client.list_database_names()
news_db = client.db
collections = news_db.list_collection_names()

def insert_mary_data(data):
    news_db["news"].insert_many(data)
    print('儲存成功')

def delete_document():
    news_db["news"].delete_many({})
    print('資料已全部刪除')

def find_all_data():
    find_data = news_db["news"].find()
    data= []
    for api in find_data:
        api['_id'] = str(api['_id'])
        data.append(api)
    return list(data)
from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("DB"))
news_db = client.db

def insert_mary_data(data):
    news_db["news"].insert_many(data)
    print('儲存成功')

def delete_document():
    news_db["news"].delete_many({})
    print('資料已全部刪除')

def find_other_data(news_name):
    find_data = news_db["news"].find({'name':news_name})
    data= []
    for api in find_data:
        api['_id'] = str(api['_id'])
        data.append(api)
    return list(data)

def find_all_data(page):
    find_data = news_db["news"].find().skip(page * 50).limit(50)
    data= []
    for api in find_data:
        api['_id'] = str(api['_id'])
        data.append(api)
    return list(data)
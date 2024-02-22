from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from database.news import find_all_data, find_other_data
import os

load_dotenv()
app = Flask(__name__)
app.json.ensure_ascii = False
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["300/day"],
)
CORS(app, resources={r'/.*': {'origins':f'{os.environ.get("URL")}'}})

@app.route('/news/<news_name>')
def other_news(news_name):
    return find_other_data(news_name)

@app.route('/news/<int:page>')
def news(page):
    return find_all_data(page)

if __name__ == '__main__':
    app.run(debug=True)
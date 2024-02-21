from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from database.news import find_all_data
import os

load_dotenv()
app = Flask(__name__)
app.json.ensure_ascii = False
CORS(app, resources={r'/.*': {'origins':f'{os.environ.get("URL")}'}})

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["1/second"],
)

@app.route('/news/<int:page>')
def news(page):
    return find_all_data(page)

if __name__ == '__main__':
    app.run(debug=True)
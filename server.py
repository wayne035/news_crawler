from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import database.news as newsdb
import os

load_dotenv()

app = Flask(__name__)
app.json.ensure_ascii = False
CORS(app, resources={r'/.*': {'origins':f'{os.environ.get("URL")}'}})

@app.route('/news')
def news():
    return newsdb.find_all_data()

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from database.news import find_all_data
import os

load_dotenv()

app = Flask(__name__)
app.json.ensure_ascii = False
CORS(app, resources={r'/.*': {'origins':f'{os.environ.get("URL")}'}})

@app.route('/news')
def news():
    return find_all_data()

if __name__ == '__main__':
    app.run(debug=True)
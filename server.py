from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.json.ensure_ascii = False
CORS(app, resources={r'/.*': {'origins':f'{os.environ.get("URL")}'}})

@app.route('/')
def news():
    return 'hello flask'

if __name__ == '__main__':
    app.run(debug=True)
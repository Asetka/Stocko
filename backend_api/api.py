from flask import Flask
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_hello():
    print("GET")
    response = {'hi': "hello world"}
    return response

@app.route('/time')
def get_time():
    print("GET")
    response = {'time': time.time()}
    return response
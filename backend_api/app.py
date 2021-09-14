from flask import Flask
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/stock-evaluation')
def get_stock_evaluation():
    print("GET")
    response = {'req': "you want a stock evaluation, req should be from frontend"}
    return response

@app.route('/personal-portfolio')
def get_personal_portfolio():
    print("GET")
    response = {'req': "you want a personal portfolio, req should be from frontend"}
    return response

@app.route('/stock-price')
def get_stock_price():
    print("GET")
    response = {'req': "you want a stock price, req should be from backend"}
    return response

@app.route('/time')
def get_time():
    print("GET")
    response = {'time': time.time()}
    return response
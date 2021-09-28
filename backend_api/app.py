from backend_processing.db_wrapper import edit_positions
from flask import Flask
from flask.wrappers import Request
from werkzeug.wrappers import request
from flask import request as rq
from flask_cors import CORS
import time
from backend_processing.backend_stock import my_main
import backend_processing.db_wrapper as db


app = Flask(__name__)
CORS(app)

@app.route('/stock-evaluation/<ticker>')
def get_stock_evaluation(ticker):
    print("GET EVALUTAIONS")
    print(ticker)
    response = my_main(ticker)
    # response = {
    #     'ticker': ticker,
    #     'req': "you want a stock evaluation, req should be from frontend"
    # }
    return response

@app.route('/personal-portfolio/<username>', methods=['GET', 'PUT', 'DELETE', 'POST'])
def get_personal_portfolio(username):
    if rq.method == 'GET':
        print('GET')
        try:
            user_response = db.get_positions(username)
            response = {username: user_response}
            return response
        except:
            return 'Could not perform GET function\nEnsure the username entered is valid'
    if rq.method == 'PUT':
        try:
            ticker = rq.form['ticker']
            avg_price = rq.form['avg_price']
            qty = rq.form['qty']
            if db.edit_positions(username, ticker, avg_price, qty) == 1:
                return ticker +  ' Updated'
            else:
                return 'Could not edit ' + ticker
        except:
            return 'Could not perform the PUT function\n Ensure the PUT body includes ticker, avg_price, and qty'
    if rq.method == 'POST':
        print('POST')
        try:
            ticker = rq.form['ticker']
            avg_price = rq.form['avg_price']
            qty = rq.form['qty']
            db.add_position(username, ticker, avg_price, qty)
            return 'Added position ' + ticker + ' successfully'
        except:
            return 'Could not perform the POST function\nEnsure your POST body is includes ticker, avg_price, and qty'

    if rq.method == 'DELETE':
        try:
            ticker = rq.form['ticker']
            if db.edit_positions(username, ticker, 0, 0) == 1:
                return ticker +  ' Deleted!'
            else:
                return 'Could not delete ' + ticker
        except:
            return 'Could not perform the DELETE function\n Ensure the DELETE body includes ticker'

    return ''

@app.route('/user/<username>', methods=['GET'])
def create_user(username):
    if db.add_user(username) == 1:
        return 'Added ' + username
    else:
        return 'Could not add user'

@app.route('/stock-price/<ticker>', methods=['GET'])
def get_stock_price(ticker):
    response = {'price': db.get_price(ticker)}
    return response

@app.route('/time')
def get_time():
    print("GET")
    response = {'time': time.time()}
    return response
from backend_api.backend_processing.db_wrapper import edit_positions
from flask import Flask
from flask.wrappers import Request
from werkzeug.wrappers import request
from flask import request as rq
from flask_cors import CORS
import time
from backend_api.backend_processing.backend_stock import my_main
import backend_api.backend_processing.db_wrapper as db


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '<h1>Home<h1>'

@app.route('/stock-evaluation/<ticker>')
def get_stock_evaluation(ticker):
    print("GET EVALUTAIONS")
    print(ticker)
    response = my_main(ticker, "PILLARS")
    #TAKE THIS CALL BELOW OUT WHEN THERE IS A FORECAST PAGE BUTTON I CAN TEST
    my_main(ticker, "FORECAST PAGE")
    return response

@app.route('/stock-page/<ticker>')
def get_stock_page(ticker):	
    print("GET STOCK PAGE")		
    print(ticker)		
    response = my_main(ticker, "STOCK PAGE")
    return response

@app.route('/forecast-page/<ticker>')
def get_forecast_page(ticker):	
    print("GET FORECAST PAGE")		
    print(ticker)		
    response = my_main(ticker, "FORECAST PAGE")
    return response


@app.route('/personal-portfolio/<username>', methods=['GET', 'PUT', 'DELETE', 'POST'])
def get_personal_portfolio(username):
    if rq.method == 'GET':
        print('GET')
        try:
            user_response = db.get_positions(username)
            response = {"response" : user_response}
            return response
        except:
            return 'Could not perform GET function\nEnsure the username entered is valid'
    if rq.method == 'PUT':
        try:
            ticker = rq.form['ticker'].upper()
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
            ticker = rq.form['ticker'].upper()
            avg_price = rq.form['avg_price']
            qty = rq.form['qty']
            db.add_position(username, ticker, avg_price, qty)
            return 'Added position ' + ticker + ' successfully'
        except:
            return 'Could not perform the POST function\nEnsure your POST body is includes ticker, avg_price, and qty'

    if rq.method == 'DELETE':
        try:
            ticker = rq.form['ticker'].upper()
            if db.edit_positions(username, ticker, 0, 0) == 1:
                return ticker +  ' Deleted!'
            else:
                return 'Could not delete ' + ticker
        except:
            return 'Could not perform the DELETE function\n Ensure the DELETE body includes ticker'

    return ''

@app.route('/user/<username>', methods=['POST'])
def create_user(username):
    if db.add_user(username) == 1:
        return 'Added ' + username
    else:
        return 'Could not add user'

@app.route('/stock-price/<ticker>', methods=['GET'])
def get_stock_price(ticker):
    price = db.get_price(ticker)
    if not price:
        return 'Price could not be retrieved'
    else:
        response = {'price': price}
    return response

@app.route('/time')
def get_time():
    print("GET")
    response = {'time': time.time()}
    return response


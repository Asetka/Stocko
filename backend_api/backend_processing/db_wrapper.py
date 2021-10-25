import pymongo
import yfinance as yf
from pymongo import collection

CLIENT = pymongo.MongoClient("mongodb+srv://App:ZU5u0b56vYc7xY15@stockopositions.r5bip.mongodb.net/StockoPositions?retryWrites=true&w=majority")
DB = CLIENT.test
USER_COLLECTION = DB.get_collection('dev-users')
PRICE_COLLECTION = DB.get_collection('dev-prices')
# db.create_collection('users')

def add_user(username):
    if not USER_COLLECTION.find_one({'username': username}):
        added_document = USER_COLLECTION.insert_one({'username': username, 'positions': []})
        return 1
    else:
        return 0

    # print(USER_COLLECTION.find_one({'username': username}))


def add_positions(username, positions): # positions format [{'ticker': 'ticker', 'avg_price': 250, 'qty': 10}, ...]
    # user_positions = USER_COLLECTION.find({'username': username}, {'positions': 1})[0]['positions']
    for pos in positions:
        add_position(username, pos['ticker'], pos['avg_price'], pos['qty'])


def add_position(username, ticker, avg_price, qty):
    add_user(username)
    positions = USER_COLLECTION.find({'username': username}, {'positions': 1})[0]['positions']
    print(positions)
    if ticker not in positions:
        positions.append({'ticker': ticker, 'avg_price': avg_price, 'qty': qty})
        USER_COLLECTION.find_one_and_update({'username': username}, {'$set' : {'positions': positions}})
        return 1
    else:
        return 0

def get_positions(username):
    add_user(username)
    positions = USER_COLLECTION.find({'username': username}, {'positions': 1})[0]['positions']
    print(positions)
    for position_index in range(len(positions)):
        qty = positions[position_index]['qty']
        avg_price = positions[position_index]['avg_price']
        price = float(get_price(positions[position_index]['ticker']))
        positions[position_index]['price'] = price
        positions[position_index]['profit'] = (float(qty)*price)-float(avg_price)*float(qty)
        positions[position_index]['pct_change'] = (price-float(avg_price))/float(avg_price)
    return positions

    #return USER_COLLECTION.find({'username': username}, {'positions': 1})[0]['positions']

def edit_positions(username, ticker, avg_price, qty):
    add_user(username)
    positions = USER_COLLECTION.find({'username': username}, {'positions': 1})[0]['positions']
    for pos in range(0, len(positions)):
        if positions[pos]['ticker'] == ticker:
            if qty == 0:
                del positions[pos]
            else:
                if avg_price:
                    positions[pos]['avg_price'] = avg_price
                if qty:
                    positions[pos]['qty'] = qty
            USER_COLLECTION.find_one_and_update({'username': username}, {'$set' : {'positions': positions}})
            return 1
    return 0

def add_ticker(ticker):
    PRICE_COLLECTION.insert_one({'ticker': ticker, 'price': 0})

def change_price(ticker, price):
    PRICE_COLLECTION.find_one_and_update({'ticker': ticker}, {'ticker': ticker, 'price': price})


def gather_active_tickers():
    all_active_tickers = []
    all_users = USER_COLLECTION.find({},{'positions': 1})
    for user in all_users:
        for pos in user['positions']:
            if not pos['ticker'] in all_active_tickers:
                all_active_tickers.append(pos['ticker'])

    print(all_active_tickers)
    return all_active_tickers

def refine_prices_db(active_tickers):
    all_prices = PRICE_COLLECTION.find({},{'positions': 1})
    for price in all_prices:
        if not price['ticker'] in active_tickers:
            PRICE_COLLECTION.delete_one({'id': price['id']})

def update_prices(active_tickers):
    for ticker in active_tickers:
        price = yf.Ticker(ticker).info['regularMarketPrice']
        if not PRICE_COLLECTION.find_one_and_update({'ticker': ticker}, {'$set': {'price': price}}):
            PRICE_COLLECTION.insert_one({'ticker': ticker, 'price': price})

        #yf.Ticker(ticker).info['regularMarketPrice']

def get_price(ticker):
    return yf.Ticker(ticker).info['regularMarketPrice']


def main(): 
    get_positions('Brady')
    # add_user('cadavis21')
    # add_user('brendanlucich')
    # add_positions('brendanlucich', [{'ticker': 'TEAM', 'qty': 10, 'avg_price': 256}, {'ticker': 'AAPL', 'qty': 20, 'avg_price': 125}])
    # update_prices(gather_active_tickers())
    # get_price('TEAM')
    # update_prices(gather_active_tickers())
    # add_user('Brady')     
    # add_positions('Brady', [{'ticker': 'TEAM', 'qty': 10, 'avg_price': 256}, {'ticker': 'AAPL', 'qty': 20, 'avg_price': 125}])
    # add_user('Brendan')
    # add_positions('Brendan', [{'ticker': 'F', 'qty': 10, 'avg_price': 256}, {'ticker': 'CRM', 'qty': 20, 'avg_price': 125}])

if __name__ == '__main__': 
    main()

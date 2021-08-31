import pymongo
from pymongo import collection

CLIENT = pymongo.MongoClient("mongodb+srv://App:ZU5u0b56vYc7xY15@stockopositions.r5bip.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB = CLIENT.test
COLLECTION = DB.get_collection('users')
# db.create_collection('users')



def add_user(username):
    if not COLLECTION.find_one({'username': username}):
        added_document = COLLECTION.insert_one({'username': username, 'positions': []})
    else:
        print('Error user exists')

    print(COLLECTION.find_one({'username': username}))


def add_positions(username, positions): # positions format [{'ticker': 'ticker', 'avg_price': 250, 'qty': 10}, ...]
    # user_positions = COLLECTION.find({'username': username}, {'positions': 1})[0]['positions']
    for pos in positions:
        add_position(username, pos['ticker'], pos['avg_price'], pos['qty'])


def add_position(username, ticker, avg_price, qty):
    positions = COLLECTION.find({'username': username}, {'positions': 1})[0]['positions']
    print(positions)
    positions.append({'ticker': ticker, 'avg_price': avg_price, 'qty': qty})
    COLLECTION.find_one_and_update({'username': username}, {'$set' : {'positions': positions}})

def get_positions(username):
    return COLLECTION.find({'username': username}, {'positions': 1})[0]['positions']

def edit_positions(username, ticker, avg_price, qty):
    positions = COLLECTION.find({'username': username}, {'positions': 1})[0]['positions']
    print(positions)
    for pos in range(0, len(positions)):
        print(pos)
        if positions[pos]['ticker'] == ticker:
            if qty == 0:
                del positions[pos]
            else:
                if avg_price:
                    positions[pos]['avg_price'] = avg_price
                if qty:
                    positions[pos]['qty'] = qty
            COLLECTION.find_one_and_update({'username': username}, {'$set' : {'positions': positions}})
            return 1
    return 0

def main():
    add_user('AndrewSetka')
    print(get_positions('AndrewSetka'))
    edit_positions('AndrewSetka', 'TEAM', 0, 0)
    print(get_positions('AndrewSetka'))
    # add_positions('AndrewSetka', [{'ticker': 'AAPL', 'avg_price': 130, 'qty': 19}, {'ticker': 'TEAM', 'avg_price': 196, 'qty': 5}, {'ticker': 'CRM', 'avg_price': 250, 'qty': 3}])
    pass



if __name__ == '__main__': 
    main()
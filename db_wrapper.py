import pymongo
from pymongo import collection

CLIENT = pymongo.MongoClient("mongodb+srv://App:ZU5u0b56vYc7xY15@stockopositions.r5bip.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB = CLIENT.test
COLLECTION = DB.get_collection('users')
# db.create_collection('users')



def make_user(username):
    added_document = COLLECTION.insert_one({'username': username})
    print(COLLECTION.find_one({'username': username}))

def add_position(username, ticker, avg_price):
    positions = COLLECTION.find({'username': username}, {'positions': 1})[0]['positions']
    print(positions)
    if not positions:
        positions = [{ticker: avg_price}]
    else:
        positions.append({ticker: avg_price})
    COLLECTION.find_one_and_update({'username': username}, {'$set' : {'positions': positions}})


def main():
    # make_user('bradym33')
    # COLLECTION.insert_one({'username': 'TestUser', 'positions': [{'ticker': 'TEAM', 'avg_price': '250'},{'ticker': 'CRM', 'avg_price': '300'} ]})
    add_position('TestUser', 'SBUX', 70)

if __name__ == '__main__': 
    main()
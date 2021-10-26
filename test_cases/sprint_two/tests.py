import requests

def print_test(test_no):
    print('TEST' + str(test_no))
    print('---------------------')

def main():

    # Testing the home page of the Heroku flask api
    print_test(1)
    if requests.get('https://stocko-flask-api-dev.herokuapp.com/').text == '<h1>Home<h1>':
        print('PASS')
    else:
        print('FAIL')

    print('')

    # Trying to get the positions of a user that doesn't exist
    print_test(2)
    if requests.get('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/idonotexist').json()['response'] == []:
        print('PASS')
    else:
        print('FAIL')

    # Ensure the stock page call returns a non-empty space
    print_test(3)
    if requests.get('https://stocko-flask-api-dev.herokuapp.com/stock-page/CRM').json():
        print('PASS')
    else:
        print('FAIL')

    # Ensure that a stock ticker passed to the API to be added or deleted is not case sensitive
    print_test(4)
    if requests.post('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/obradymack', {'ticker': 'TSLA', 'avg_price': 900, 'qty': 100}).text == 'Added position ' + 'TSLA' + ' successfully':
        print('PASS')
    else:
        print('FAIL')

    # Attempt to delete position with different casing as previous test
    print_test(5)

    if requests.delete('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/obradymack', data={'ticker': 'tsla'}).text == 'TSLA Deleted!':
        print('PASS')
    else:
        print('FAIL')

if __name__ == '__main__':
    main()

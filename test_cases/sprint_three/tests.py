import requests

def print_test(test_no):
    print('TEST' + str(test_no))
    print('---------------------')

def main():

    # Reject ticker that does not exist
    print_test(1)
    if requests.post('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/obradymack', {'ticker': 'FLOWERS', 'avg_price': 900, 'qty': 100}).text == 'Added position ' + 'FLOWERS' + ' successfully':
        print('FAIL')
    else:
        print('PASS')

    # Test a duplicate ticker
    print_test(2)
    requests.post('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/obradymack', {'ticker': 'IBM', 'avg_price': 900, 'qty': 100})
    if requests.post('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/obradymack', {'ticker': 'IBM', 'avg_price': 900, 'qty': 100}).text == 'Added position ' + 'IBM' + ' successfully':
        print('PASS')
    else:
        print('FAIL')
    # Delete the ticker to clean-up
    requests.delete('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/obradymack', data={'ticker': 'ibm'})

    print_test(3)
    if requests.delete('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/obradymack', data={'ticker': 'CARS'}).text != 'Could not delete ' + 'CARS':
        print('FAIL')
    else:
        print('PASS')

    print_test(4)
    if requests.get('https://stocko-flask-api-dev.herokuapp.com/stock-page/TSLA').text != '':
        print('PASS')
    else:
        print('FAIL')

    print_test(5)
    if requests.get('https://stocko-flask-api-dev.herokuapp.com/time') == '':
        print('FAIl')
    else:
        print('PASS')

if __name__ == '__main__':
    main()

import requests

def print_test(test_no):
    print('TEST' + str(test_no))
    print('---------------------')

def main():

    # Reject ticker that does not exist
    print_test(1)
    if requests.post('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/obradymack', {'ticker': 'FLOWERS', 'avg_price': 900, 'qty': 100}).text == 'Added position ' + 'TSLA' + ' successfully':
        print('PASS')
    else:
        print('FAIL')

    # Test a duplicate ticker
    print_test(2)
    requests.post('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/obradymack', {'ticker': 'IBM', 'avg_price': 900, 'qty': 100})
    if requests.post('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/obradymack', {'ticker': 'IBM', 'avg_price': 900, 'qty': 100}).text == 'Added position ' + 'IBM' + ' successfully':
        print('FAIL')
    else:
        print('PASS')
    # Delete the ticker to clean-up
    requests.delete('https://stocko-flask-api-dev.herokuapp.com/personal-portfolio/obradymack', data={'ticker': 'ibm'})

if __name__ == '__main__':
    main()

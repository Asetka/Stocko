import requests

def print_test(test_no):
    print('TEST' + str(test_no))
    print('---------------------')

def api_tests():

    ### TEST GETTING PRICES
    print_test(1)
    if not requests.get('http://127.0.0.1:5000/stock-price/TEAM').text == 'Price could not be retrieved':
        print('PASS')
    else:
        print('FAIL')
    print('')
    
    print_test(2)
    if not requests.get('http://127.0.0.1:5000/stock-price/TEAMER').text == 'Price could not be retrieved':
        print('FAIL')
    else:
        print('PASS')
    print('')

    ### TEST GETTING POSITIONS
    print_test(3)
    if not requests.get('http://127.0.0.1:5000/personal-portfolio/brendanlucich').text == 'Could not perform GET function\nEnsure the username entered is valid':
        print('PASS')
    else:
        print('FAIL')
    print('')

    print_test(4)
    if requests.get('http://127.0.0.1:5000/personal-portfolio/brendanlucich23').text == 'Could not perform GET function\nEnsure the username entered is valid':
        print('PASS')
    else:
        print('FAIL')
    print('')

    
    ### CREATE USER, CREATE POSITION, DELETE POSITION
    print_test(5)
    if requests.post('http://127.0.0.1:5000/user/MichaelJordan').text == 'Added MichaelJordan':
        print('PASS PART 1')
    else: 
        print('FAIL PART 1')
    print('')

    if requests.post('http://127.0.0.1:5000/personal-portfolio/MichaelJordan', {'ticker': 'F', 'avg_price': 15, 'qty': 100}).text == 'Added position ' + 'F' + ' successfully':
        print('PASS PART 2')
    else:
        print('FAIL PART 2')
    print('')

    if requests.delete('http://127.0.0.1:5000/personal-portfolio/MichaelJordan', data={'ticker': 'F'}).text == 'F Deleted!':
        print('PASS PART 3')
    else:
        print('FAIL PART 3')


### ALL TESTS VERIFIED PASSED IN DB UI 🔥

def main():
    api_tests()

if __name__ == '__main__':
    main()
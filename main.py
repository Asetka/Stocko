import json
from six.moves.urllib.request import urlopen
from functools import wraps
from backend_api.backend_processing.db_wrapper import edit_positions
from flask import Flask, jsonify, _request_ctx_stack
from flask.wrappers import Request
from werkzeug.wrappers import request
from flask import request as rq
from flask_cors import CORS, cross_origin
from jose import jwt
import time
from backend_api.backend_processing.backend_stock import my_main
import backend_api.backend_processing.db_wrapper as db

AUTH0_DOMAIN = 'dev-919y6k1x.us.auth0.com'
API_AUDIENCE = "https://stocko-flask-api-dev.herokuapp.com/"
ALGORITHMS = ["RS256"]

app = Flask(__name__)
CORS(app)

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

# Format error response and append status code
def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "Authorization header is expected"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must start with"
                            " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)

    token = parts[1]
    return token

def requires_auth(f):
    """Determines if the Access Token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer="https://"+AUTH0_DOMAIN+"/"
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                "description": "token is expired"}, 401)
            except jwt.JWTClaimsError:
                raise AuthError({"code": "invalid_claims",
                                "description":
                                    "incorrect claims,"
                                    "please check the audience and issuer"}, 401)
            except Exception:
                raise AuthError({"code": "invalid_header",
                                "description":
                                    "Unable to parse authentication"
                                    " token."}, 401)

            _request_ctx_stack.top.current_user = payload
            return f(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                        "description": "Unable to find appropriate key"}, 401)
    return decorated

def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    token = get_token_auth_header()
    unverified_claims = jwt.get_unverified_claims(token)
    if unverified_claims.get("scope"):
            token_scopes = unverified_claims["scope"].split()
            for token_scope in token_scopes:
                if token_scope == required_scope:
                    return True
    return False

@app.route('/')
def index():
    return '<h1>Home<h1>'

@app.route('/stock-evaluation/<ticker>')
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_stock_evaluation(ticker):
    print("GET EVALUTAIONS")
    print(ticker)
    response = my_main(ticker, "PILLARS")
    return response

@app.route('/stock-page/<ticker>')
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_stock_page(ticker):	
    print("GET STOCK PAGE")		
    print(ticker)		
    response = my_main(ticker, "STOCK PAGE")
    return response

@app.route('/forecast-page/<ticker>')
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_forecast_page(ticker):	
    print("GET FORECAST PAGE")		
    print(ticker)		
    response = my_main(ticker, "FORECAST PAGE")
    return response


@app.route('/personal-portfolio/<username>', methods=['GET', 'PUT', 'DELETE', 'POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
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
                print(ticker, 'Updated')
                return ticker +  ' Updated'
            else:
                print('Could not edit', ticker)
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
            print('Added position', ticker)
            return 'Added position ' + ticker + ' successfully'
        except:
            print('could not perform post function')
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
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def create_user(username):
    if db.add_user(username) == 1:
        return 'Added ' + username
    else:
        return 'Could not add user'

@app.route('/stock-price/<ticker>', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
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

#This is the format to follow for privatizing and locking requests behind roles
""" This doesn't need authentication
@app.route("/api/public")
@cross_origin(headers=["Content-Type", "Authorization"])
def public():
    response = "Hello from a public endpoint! You don't need to be authenticated to see this."
    return jsonify(message=response)

# This needs authentication
@app.route("/api/private")
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def private():
    response = "Hello from a private endpoint! You need to be authenticated to see this."
    return jsonify(message=response)

# This needs authorization
@app.route("/api/private-scoped")
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def private_scoped():
    if requires_scope("read:messages"):
        response = "Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this."
        return jsonify(message=response)
    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource"
    }, 403)
    """

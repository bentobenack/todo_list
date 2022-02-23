from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signup', methods=['POST'])
def signup():
    return "hello Auth"


@auth.route('/login', methods=['POST'])
def login():
    return "hello Auth"


@auth.route('/refresh', methods=['POST'])
def refres_token():
    return {"token": "Token"}
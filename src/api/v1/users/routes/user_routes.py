from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('/', methods=['GET'])
def get_users():
    return "hello users"
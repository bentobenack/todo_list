from flask import Blueprint

todo = Blueprint('todo', __name__, url_prefix='/todos')

@todo.route('/', methods=['GET'])
def get_todos():
    return "hello todos"
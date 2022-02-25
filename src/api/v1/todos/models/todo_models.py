from flask_restx import fields
from ..routes.todo_routes import todo

todo_model = todo.model('Todo', {
    'id': fields.String(required=True, description='The user identifier'),
    'description': fields.String(required=True, description='The to-do description'),
})

TODOS = [
    {'id': 1, 'description': 'Correr 4km'},
]
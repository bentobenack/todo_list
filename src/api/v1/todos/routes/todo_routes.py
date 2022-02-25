from flask_restx import Resource
from .import todo
from ..models.todo_models import TODOS, todo_model


@todo.route('/')
class TodoList(Resource):
    @todo.doc('list_todo')
    @todo.marshal_list_with(todo_model)
    def get(self):
        '''List all To-Dos'''
        return TODOS
    
    
@todo.route('/<id>')
@todo.param('id', 'The todo identifier')
@todo.response(404, 'Todo not found')
class Todo(Resource):
    @todo.doc('get_todo')
    @todo.marshal_with(todo_model)
    def get(self, id):
        '''Fetch a todo given its identifier'''
        for td in TODOS:
            if td['id'] == int(id):
                return td
    
        todo.abort(404)

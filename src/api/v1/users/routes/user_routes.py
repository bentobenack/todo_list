from flask_restx import Resource
from .import user
from ..models.user_models import USERS, user_model


@user.route('/')
class UserList(Resource):
    @user.doc('list_user')
    @user.marshal_list_with(user_model)
    def get(self):
        '''List all users'''
        return USERS
    
    
@user.route('/<id>')
@user.param('id', 'The user identifier')
@user.response(404, 'User not found')
class User(Resource):
    @user.doc('get_user')
    @user.marshal_with(user_model)
    def get(self, id):
        '''Fetch a user given its identifier'''
        for usr in USERS:
            if usr['id'] == int(id):
                return usr
    
        user.abort(404)

from flask_restx import Resource
from .import auth


@auth.route('/signup')
class Signup(Resource):
    @auth.doc('signup')
    def post(self):
        '''Signup in the app'''
        return "Signup"
    
    
@auth.route('/login')
class Login(Resource):
    @auth.doc('login')
    def post(self):
        '''Login in the app'''
        return "Login"
    

@auth.route('/refresh')
class RefreshToken(Resource):
    @auth.doc('refresh_token')
    def post(self):
        '''Refresh Token'''
        return "Refresh Token"

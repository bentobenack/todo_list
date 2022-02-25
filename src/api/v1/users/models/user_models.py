from flask_restx import fields
from ..routes.user_routes import user

user_model = user.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'name': fields.String(required=True, description='The user name'),
})

USERS = [
    {'id': 1, 'name': 'Felix'},
]
import os
from flask import Flask
from .api.v1.users.routes.user_routes import user
from .api.v1.auth.routes.auth_routes import auth
from .api.v1.todos.routes.todos_routes import todo
# from flask_bcrypt import Bcrypt

# flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ["DEVELOPMENT_CONFIG_SETUP"]
    app.config.from_object(environment_configuration)
    
    
    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(todo)
    # flask_bcrypt.init_app(app)
    

    return app
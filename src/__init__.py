import os
from flask import Flask
from flask_restx import Api
from .api.v1.users.routes.user_routes import user
from .api.v1.auth.routes.auth_routes import auth
from .api.v1.todos.routes.todo_routes import todo
# from flask_bcrypt import Bcrypt

# flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ["DEVELOPMENT_CONFIG_SETUP"]
    app.config.from_object(environment_configuration)
    
    api = Api(
        app=app,
        version='0.1',
        title="TodoList API",
        doc="/docs",
        description="This is the TodoList API that allow you create an todo app",
    )
    
    
    api.add_namespace(ns=user, path="/users")
    api.add_namespace(ns=todo, path="/todos")
    api.add_namespace(ns=auth, path="/refresh")
    # flask_bcrypt.init_app(app)
    
    
    return app
from flask_restx import Namespace

user = Namespace(
    name="user",
    description="Users related operations"
)
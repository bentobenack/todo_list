from flask_restx import Namespace

todo = Namespace(
    name="todo",
    description="To-do related operations"
)
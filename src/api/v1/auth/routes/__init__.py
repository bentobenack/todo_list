from flask_restx import Namespace

auth = Namespace(
    name="auth",
    description="authentication related operations"
)
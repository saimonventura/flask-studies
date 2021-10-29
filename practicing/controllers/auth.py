from flask_jwt import JWT
from resources.user import UserRegister
from security import authenticate, identity


def AuthController(app, api):
    jwt = JWT(app, authenticate, identity)  # /auth
    api.add_resource(UserRegister, '/register')
    pass

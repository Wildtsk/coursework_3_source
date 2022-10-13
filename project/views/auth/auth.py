

from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.tools.security import generate_tokens

api = Namespace('auth')


@api.route('/register')
class RegisterView(Resource):
    @api.response(model=user, as_list=True, code=200, description='ok')
    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.create_user(data.get('email'), data.get('password')), 201
        else:
            return "Чего то не хватает", 401

    @api.response(404, 'Not Found')
    def put(self):
        data = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        return user_service.get_user_by_token(refresh_token=header)


@api.route('/login/')
class LoginView(Resource):

    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            user = user_service.get_user_by_login(data.get('email'))
            return generate_tokens(user.email, data.get('password'), password_hash=user.password, is_refresh=False)

        else:
            return "Чего то не хватает", 401

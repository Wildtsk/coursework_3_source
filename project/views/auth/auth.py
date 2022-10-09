from importlib.resources import Resource

from flask import request
from flask_restx import Namespace

from project.container import user_service
from project.setup.api.models import user

api = Namespace('auth')


@api.route('/register')
class RegisterView(Resource):
    @api.response(user, as_list=True, code=200, description='ok')
    def path(self):
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


@api.route('/password/')
class LoginView(Resource):

    def put(self):
        data = request.json
        if data.get('access_token') and data.get('refresh_token'):
            return user_service.update_token(data.get('refresh_token')), 201
        else:
            return "Чего то не хватает", 401

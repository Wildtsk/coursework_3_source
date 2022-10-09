from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Петров'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Омерзительная восьмерка'),
    'description': fields.String(required=True, max_length=100, example='США после Гражданской войны.'),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=lmB9VWm0okU'),
    'year': fields.Integer(required=True, max_length=100),
    'rating': fields.Float(required=True, max_length=100),
    'genre_id': fields.Nested(genre),
    'director_id': fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='serg@mail.ru'),
    'password': fields.String(required=True, max_length=100, example='198365'),
    'name': fields.String(required=True, max_length=100, example='Serg'),
    'surname': fields.String(required=True, max_length=100, example='Yakim'),
    'favorite_genre ': fields.Nested(genre)
})
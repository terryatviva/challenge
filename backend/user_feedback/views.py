from flask import jsonify
from flask_restful import Api, Resource, reqparse, inputs
from user_feedback import app,db
from .models import User
from .utils import valid_email, valid_string

import datetime

user_parser = reqparse.RequestParser()
user_parser.add_argument('name',type=valid_string,nullable=False,required=True)
user_parser.add_argument('date_of_birth',type=inputs.date,nullable=False,required=True)
user_parser.add_argument('email',type=valid_email,nullable=False,required=True)
user_parser.add_argument('country',type=valid_string,nullable=False,required=True)
user_parser.add_argument('city',type=valid_string,nullable=False,required=True)
user_parser.add_argument('likes',type=valid_string,nullable=False,required=True)
user_parser.add_argument('dislikes',type=valid_string,nullable=False,required=True)

class UserList(Resource):
    def get(self):
        users = User.query.all()
        return jsonify({
            'users': [user.serialized for user in users]
        })
    
    def post(self):
        args = user_parser.parse_args()
        user = User(
            name=args['name'],
            date_of_birth=args['date_of_birth'],
            email=args['email'],
            country=args['country'],
            city=args['city'],
            likes=args['likes'],
            dislikes=args['dislikes']
        )

        db.session.add(user)
        db.session.commit()

        return jsonify(user.serialized)

api = Api(app)
api.add_resource(UserList,'/users')

if __name__ == '__main__':
    app.run(debug=True)
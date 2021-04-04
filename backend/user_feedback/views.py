from flask import jsonify, make_response
from flask_restful import Api, Resource, reqparse, inputs
from user_feedback import app, db
from .models import User
from .utils import valid_email, valid_string

# Validate arguments 
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=valid_string,nullable=False, required=True)
user_parser.add_argument('date_of_birth', type=inputs.date, nullable=False, required=True)
user_parser.add_argument('email', type=valid_email, nullable=False, required=True)
user_parser.add_argument('country', type=valid_string, nullable=False, required=True)
user_parser.add_argument('city', type=valid_string, nullable=False, required=True)
user_parser.add_argument('likes', type=valid_string, nullable=False, required=True)
user_parser.add_argument('dislikes', type=valid_string, nullable=False, required=True)


class UserList(Resource):

    def get(self):
        # Retrieve all saved users 
        users = User.query.all()
        response = make_response(
            jsonify({
                'users': [user.serialized for user in users]
            })
        )

        response.status_code = 200

        return response

    def post(self):
        # Get arguments
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

        # Saves the user to the database
        db.session.add(user)
        db.session.commit()

        response = make_response(
            jsonify(user.serialized)
        )

        response.status_code = 200

        return response

api = Api(app)
api.add_resource(UserList, '/users')

# Add the necessary headers after every request to avoid CORS errors
@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers,' +
                                                        'Origin, X-Requested-With, Content-Type,'+ 
                                                        'Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
    response.headers['Access-Control-Expose-Headers'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)

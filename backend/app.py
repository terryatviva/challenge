from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json

app = Flask(__name__, static_folder = './public', template_folder="./static")
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column('ID', db.Integer, primary_key=True)
    username = db.Column('Name', db.String(80), nullable=False)
    email = db.Column('Email', db.String(120), nullable=False)
    city = db.Column('City', db.String(120), nullable=False)
    country = db.Column('Country', db.String(120), nullable=False)
    date_of_birth = db.Column('Date_Of_Birth', db.String(120), nullable=False)
    like = db.Column('Like', db.String(120), nullable=False)
    dislike = db.Column('Dislike', db.String(120), nullable=False)

    @staticmethod
    def insert_into_user_account(username, email, city, country, date_of_birth, like, dislike):
        user_acc_obj = User(username=username, email=email, city=city, country=country, date_of_birth=date_of_birth,
                            like=like, dislike=dislike)
        db.session.add(user_acc_obj)
        db.session.flush()


parser = reqparse.RequestParser()
parser.add_argument('data')


class SubmitForm(Resource):
    def post(self):
        args =  parser.parse_args()
        user = json.loads(args.data)
        try:
            User.insert_into_user_account(
                username=user['name'],
                email=user['email'],
                city=user['city'],
                country=user['country'],
                date_of_birth=user['DOB'],
                like=user['like'],
                dislike=user['dislike']
            )
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            return {'status': 400, 'message': 'Invalid data'}

        return jsonify(args)


class ListData(Resource):
    def get(self):
        data = User.query.all()
        json_res = []
        for result in data:
            temp_obj = {}
            temp_obj['id'] = result.id
            temp_obj['name'] = result.username
            temp_obj['email'] = result.email
            temp_obj['city'] = result.city
            temp_obj['country'] = result.country
            temp_obj['Date Of Birth'] = result.date_of_birth
            temp_obj['like'] = result.like
            temp_obj['dislike'] = result.dislike
            json_res.append(temp_obj)

        return jsonify(json_res)


api.add_resource(SubmitForm, '/submit')
api.add_resource(ListData, '/list')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=4000, host="127.0.0.1")
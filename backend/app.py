from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        args =  parser.parse_args()
        return jsonify(args)


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

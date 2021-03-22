from flask import Flask,request
from feedback_api import FeedbackApi
from flask_restful import Api
from models import db


app = Flask(__name__)

api = Api(app)
# set database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# Connect to the following signals to get notified before and after changes are committed to the database is not needed in current use case
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app(app)


api.add_resource(FeedbackApi, "/feedback")

if __name__ == "__main__":
  app.run(debug=True)

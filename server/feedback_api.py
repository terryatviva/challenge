from flask import Flask, request
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with
from datetime import date
from models import FeedbackModel, db


# define a request parser for the Feedback sent from the client
# and to make validation upon client request
feedback_post_args = reqparse.RequestParser()
feedback_post_args.add_argument("name", type=str, help="No data", required=True)
feedback_post_args.add_argument("birth_date", type=inputs.date, help="No data", required=True)
feedback_post_args.add_argument('email_address', type=inputs.regex('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'), required=True)
feedback_post_args.add_argument("country", type=str, help="No data", required=True)
feedback_post_args.add_argument("city", type=str, help="No data", required=True)
feedback_post_args.add_argument("good_comment", type=str, help="No data", required=True)
feedback_post_args.add_argument("bad_comment", type=str, help="No data", required=True)

class FeedbackApi(Resource):
  def get(self):
    feedback_list = FeedbackModel.query.all()
    feedbacks = []
    for feedback in feedback_list:
      feedbacks.append(
        {
          'id' : feedback.id,
          'name' : feedback.name,
          'birth_date' : str(feedback.birth_date),
          'email_address' : feedback.email_address,
          'country' : feedback.country,
          'city' : feedback.city,
          'good_comment' : feedback.good_comment,
          'bad_comment' : feedback.bad_comment,
        }
      )
    return feedbacks

  def post(self):
    args = feedback_post_args.parse_args()
    
    new_feedback = FeedbackModel(
      name=args['name'], 
      birth_date=args['birth_date'],
      email_address=args['email_address'],
      country=args['country'],
      city=args['city'],
      good_comment=args['good_comment'],
      bad_comment=args['bad_comment'],
    )
    db.session.add(new_feedback)
    db.session.commit()
    
    return {"message" : "Posted"}
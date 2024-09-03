from flask import Flask, request
from flask_restful import Resource, Api
from myapp import create_app, db
from myapp.models import User  # Assuming User model is in models.py

app = create_app()
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class UserResource(Resource):
    def post(self):
        data = request.get_json()
        full_name = data.get('full_name')
        email = data.get('email')
        password = data.get('password')
        subscription = data.get('subscription')

        if full_name and email and password and subscription:
            new_user = User(full_name=full_name, email=email, password=password, subscription=subscription)

            try:
                db.session.add(new_user)
                db.session.commit()
                return {"message": "User created successfully"}, 201
            except Exception as e:
                db.session.rollback()
                return {"message": f"An error occurred: {str(e)}"}, 500
        else:
            return {"message": "Missing required fields"}, 400

api.add_resource(UserResource, '/user')

# Placeholder for other resources
class NewsResource(Resource):
    pass

class DocumentationResource(Resource):
    pass

class MultimediaResource(Resource):
    pass

class PodcastResource(Resource):
    pass

class PanelDiscussionResource(Resource):
    pass

class InterviewResource(Resource):
    pass

# Add additional resources as needed
api.add_resource(NewsResource, '/news')
api.add_resource(DocumentationResource, '/documentation')
api.add_resource(MultimediaResource, '/multimedia')
api.add_resource(PodcastResource, '/podcast')
api.add_resource(PanelDiscussionResource, '/panel-discussion')
api.add_resource(InterviewResource, '/interview')

if __name__ == '__main__':
    app.run(debug=True, port=5500)

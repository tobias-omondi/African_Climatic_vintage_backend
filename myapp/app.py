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

        # Extract required fields
        full_name = data.get('full_name')
        email = data.get('email')
        message = data.get('message')

        # Check if all required fields are provided
        if not full_name or not email or not message:
            return {"message": "Missing required fields: full_name, email, or message"}, 400

        # Create a new User instance
        new_user = User(full_name=full_name, email=email, message=message)

        try:
            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()
            return {"message": "User created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

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

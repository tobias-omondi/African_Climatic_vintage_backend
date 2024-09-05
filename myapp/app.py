from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_login import login_user, logout_user, current_user, login_required
from myapp import create_app, db, bcrypt
from myapp.models import User, AdminUser, News, Documentation,Multimedia,Podcast, PanelDiscussion, Interview


app = create_app()
api = Api(app)
# Existing HelloWorld and UserResource

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class UserResource(Resource):
    def post(self):
        data = request.get_json()

        full_name = data.get('full_name')
        email = data.get('email')
        message = data.get('message')

        if not full_name or not email or not message:
            return {"message": "Missing required fields: full_name, email, or message"}, 400

        new_user = User(full_name=full_name, email=email, message=message)

        try:
            db.session.add(new_user)
            db.session.commit()
            return {"message": "User created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

api.add_resource(UserResource, '/user')

class NewsResource(Resource):
    # Create a new news item (POST)
    def post(self):
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        image_url = data.get('image_url')
        admin_id = data.get('admin_id')

        if not title or not description:
            return {"message": "Title and description are required"}, 400

        new_news = News(
            title=title,
            description=description,
            image_url=image_url,
            admin_id=admin_id
        )

        try:
            db.session.add(new_news)
            db.session.commit()
            return {"message": "News item created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Update an existing news item (PUT)
    def put(self, news_id):
        news_item = News.query.get_or_404(news_id)
        data = request.get_json()

        news_item.title = data.get('title', news_item.title)
        news_item.description = data.get('description', news_item.description)
        news_item.image_url = data.get('image_url', news_item.image_url)

        try:
            db.session.commit()
            return {"message": "News item updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Delete a news item (DELETE)
    def delete(self, news_id):
        news_item = News.query.get_or_404(news_id)

        try:
            db.session.delete(news_item)
            db.session.commit()
            return {"message": "News item deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

api.add_resource(NewsResource, '/news', '/news/<int:news_id>')

class DocumentationResource(Resource):
    # Create a new documentation item (POST)
    def post(self):
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        content_type = data.get('content_type')
        file_path = data.get('file_path')
        file_url = data.get('file_url')
        admin_id = data.get('admin_id')

        if not title or not description:
            return {"message": "Title and description are required"}, 400

        new_documentation = Documentation(
            title=title,
            description=description,
            content_type=content_type,
            file_path=file_path,
            file_url=file_url,
            admin_id=admin_id
        )

        try:
            db.session.add(new_documentation)
            db.session.commit()
            return {"message": "Documentation item created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Update an existing documentation item (PUT)
    def put(self, doc_id):
        documentation_item = Documentation.query.get_or_404(doc_id)
        data = request.get_json()

        documentation_item.title = data.get('title', documentation_item.title)
        documentation_item.description = data.get('description', documentation_item.description)
        documentation_item.content_type = data.get('content_type', documentation_item.content_type)
        documentation_item.file_path = data.get('file_path', documentation_item.file_path)
        documentation_item.file_url = data.get('file_url', documentation_item.file_url)

        try:
            db.session.commit()
            return {"message": "Documentation item updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Delete a documentation item (DELETE)
    def delete(self, doc_id):
        documentation_item = Documentation.query.get_or_404(doc_id)

        try:
            db.session.delete(documentation_item)
            db.session.commit()
            return {"message": "Documentation item deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

api.add_resource(DocumentationResource, '/documentation', '/documentation/<int:doc_id>')


class MultimediaResource(Resource):
    # Create a new multimedia item (POST)
    def post(self):
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        content_type = data.get('content_type')
        file_path = data.get('file_path')
        file_url = data.get('file_url')
        admin_id = data.get('admin_id')

        if not title:
            return {"message": "Title is required"}, 400

        if not content_type:
            return {"message": "Content type is required"}, 400

        new_multimedia = Multimedia(
            title=title,
            description=description,
            content_type=content_type,
            file_path=file_path,
            file_url=file_url,
            admin_id=admin_id
        )

        try:
            db.session.add(new_multimedia)
            db.session.commit()
            return {"message": "Multimedia item created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Update an existing multimedia item (PUT)
    def put(self, multimedia_id):
        multimedia_item = Multimedia.query.get_or_404(multimedia_id)
        data = request.get_json()

        multimedia_item.title = data.get('title', multimedia_item.title)
        multimedia_item.description = data.get('description', multimedia_item.description)
        multimedia_item.content_type = data.get('content_type', multimedia_item.content_type)
        multimedia_item.file_path = data.get('file_path', multimedia_item.file_path)
        multimedia_item.file_url = data.get('file_url', multimedia_item.file_url)

        try:
            db.session.commit()
            return {"message": "Multimedia item updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Delete a multimedia item (DELETE)
    def delete(self, multimedia_id):
        multimedia_item = Multimedia.query.get_or_404(multimedia_id)

        try:
            db.session.delete(multimedia_item)
            db.session.commit()
            return {"message": "Multimedia item deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

api.add_resource(MultimediaResource, '/multimedia', '/multimedia/<int:multimedia_id>')


class PodcastResource(Resource):
    # Create a new podcast (POST)
    def post(self):
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        audio_url = data.get('audio_url')
        admin_id = data.get('admin_id')

        if not title or not audio_url:
            return {"message": "Title and audio URL are required"}, 400

        new_podcast = Podcast(
            title=title,
            description=description,
            audio_url=audio_url,
            admin_id=admin_id
        )

        try:
            db.session.add(new_podcast)
            db.session.commit()
            return {"message": "Podcast created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Update an existing podcast (PUT)
    def put(self, podcast_id):
        podcast = Podcast.query.get_or_404(podcast_id)
        data = request.get_json()

        podcast.title = data.get('title', podcast.title)
        podcast.description = data.get('description', podcast.description)
        podcast.audio_url = data.get('audio_url', podcast.audio_url)

        try:
            db.session.commit()
            return {"message": "Podcast updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Delete a podcast (DELETE)
    def delete(self, podcast_id):
        podcast = Podcast.query.get_or_404(podcast_id)

        try:
            db.session.delete(podcast)
            db.session.commit()
            return {"message": "Podcast deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

api.add_resource(PodcastResource, '/podcast', '/podcast/<int:podcast_id>')


class PanelDiscussionResource(Resource):
    # Create a new panel discussion (POST)
    def post(self):
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        panel_list = data.get('panel_list')
        video_file_path = data.get('video_file_path')
        admin_id = data.get('admin_id')

        if not title:
            return {"message": "Title is required"}, 400

        new_panel_discussion = PanelDiscussion(
            title=title,
            description=description,
            panel_list=panel_list,
            video_file_path=video_file_path,
            admin_id=admin_id
        )

        try:
            db.session.add(new_panel_discussion)
            db.session.commit()
            return {"message": "Panel Discussion created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Update an existing panel discussion (PUT)
    def put(self, paneldiscussion_id):
        panel_discussion = PanelDiscussion.query.get_or_404(paneldiscussion_id)
        data = request.get_json()

        panel_discussion.title = data.get('title', panel_discussion.title)
        panel_discussion.description = data.get('description', panel_discussion.description)
        panel_discussion.panel_list = data.get('panel_list', panel_discussion.panel_list)
        panel_discussion.video_file_path = data.get('video_file_path', panel_discussion.video_file_path)

        try:
            db.session.commit()
            return {"message": "Panel Discussion updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Delete a panel discussion (DELETE)
    def delete(self, paneldiscussion_id):
        panel_discussion = PanelDiscussion.query.get_or_404(paneldiscussion_id)

        try:
            db.session.delete(panel_discussion)
            db.session.commit()
            return {"message": "Panel Discussion deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

api.add_resource(PanelDiscussionResource, '/panel-discussion', '/panel-discussion/<int:paneldiscussion_id>')

class InterviewResource(Resource):
    # Create a new interview item (POST)
    def post(self):
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        image_url = data.get('image_url')
        admin_id = data.get('admin_id')

        if not title or not image_url:
            return {"message": "Title and image_url are required"}, 400

        new_interview = Interview(
            title=title,
            description=description,
            image_url=image_url,
            admin_id=admin_id
        )

        try:
            db.session.add(new_interview)
            db.session.commit()
            return {"message": "Interview item created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Update an existing interview item (PUT)
    def put(self, interview_id):
        interview_item = Interview.query.get_or_404(interview_id)
        data = request.get_json()

        interview_item.title = data.get('title', interview_item.title)
        interview_item.description = data.get('description', interview_item.description)
        interview_item.image_url = data.get('image_url', interview_item.image_url)

        try:
            db.session.commit()
            return {"message": "Interview item updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

    # Delete an interview item (DELETE)
    def delete(self, interview_id):
        interview_item = Interview.query.get_or_404(interview_id)

        try:
            db.session.delete(interview_item)
            db.session.commit()
            return {"message": "Interview item deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500
            

api.add_resource(InterviewResource, '/interview', '/interview/<int:interview_id>')


# New Admin Resources
class AdminLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"message": "Missing required fields: username or password"}, 400

        admin_user = AdminUser.query.filter_by(username=username).first()
        if not admin_user:
            return {"message": "User not found"}, 404

        if bcrypt.check_password_hash(admin_user.password, password):
            login_user(admin_user)
            return {"message": "Login successful"}, 200
        return {"message": "Invalid credentials"}, 401

api.add_resource(AdminLogin, '/admin/login')

class CreateAdmin(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"message": "Username and password are required"}, 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            new_admin = AdminUser(username=username, password=hashed_password, is_admin=True)
            db.session.add(new_admin)
            db.session.commit()
            return {"message": "Admin user created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

api.add_resource(CreateAdmin, '/admin/create')


class AuthStatus(Resource):
    def get(self):
        if current_user.is_authenticated:
            return {
                'isAuthenticated': True,
                'user': {
                    'username': current_user.username,
                    'isAdmin': current_user.is_admin
                }
            }
        return {'isAuthenticated': False}, 200

api.add_resource(AuthStatus, '/auth/status')

class ChangePassword(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        current_password = data.get('current_password')
        new_password = data.get('new_password')

        if not username or not current_password or not new_password:
            return {"message": "Missing required fields: username, current_password, or new_password"}, 400

        # Fetch the admin user
        admin_user = AdminUser.query.filter_by(username=username).first()
        if not admin_user:
            return {"message": "User not found"}, 404

        # Check if the current password is correct
        if not bcrypt.check_password_hash(admin_user.password, current_password):
            return {"message": "Current password is incorrect"}, 401

        # Set the new password
        admin_user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        db.session.commit()
        return {"message": "Password updated successfully"}, 200

api.add_resource(ChangePassword, '/admin/change-password')


if __name__ == '__main__':
    app.run(debug=True, port=5500)

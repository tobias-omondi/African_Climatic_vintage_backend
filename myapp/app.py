from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_login import login_user, logout_user, current_user, login_required
from myapp import create_app, db, bcrypt
from myapp.models import User, AdminUser

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


if __name__ == '__main__':
    app.run(debug=True, port=5500)

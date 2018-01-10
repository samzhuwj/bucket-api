from app import db, bcrypt
from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from app.models import User
import re

auth = Blueprint('auth', __name__)


class RegisterUser(MethodView):
    """
    View function to register a user via the api
    """
    def post(self):
        if request.content_type == 'application/json':
            post_data = request.get_json()
            email = post_data.get('email')
            password = post_data.get('password')
            if re.match(r"[^@]+@[^@]+\.[^@]+", email) and len(password) > 4:
                user = User.query.filter_by(email=email).first()
                if not user:
                    user = User(email=email, password=password)
                    db.session.add(user)
                    db.session.commit()
                    auth_token = user.encode_auth_token(user_id=user.id)
                    response = {
                        'status': 'success',
                        'message': 'Successfully registered',
                        'auth_token': auth_token.decode("utf-8")
                    }
                    return make_response(jsonify(response)), 201

                else:
                    response = {
                        'status': 'failed',
                        'message': 'Failed, User already exists, Please sign In'
                    }
                    return make_response(jsonify(response)), 202
            return make_response(
                jsonify({'status': 'failed',
                         'message': 'Missing or wrong email format or password is less than four characters'})), 202
        return make_response(jsonify({'status': 'failed', 'message': 'Content-type must be json'})), 202


class LoginUser(MethodView):
    def post(self):
        if request.content_type == 'application/json':
            post_data = request.get_json()
            email = post_data.get('email')
            password = post_data.get('password')
            if re.match(r"[^@]+@[^@]+\.[^@]+", email) and len(password) > 4:
                user = User.query.filter_by(email=email).first()
                if user and bcrypt.check_password_hash(user.password, password):
                    auth_token = user.encode_auth_token(user.id)
                    return make_response(jsonify({
                        'status': 'success',
                        'auth_token': auth_token.decode(),
                        'message': 'Successfully logged In'
                    }))
                return make_response(
                    jsonify({'status': 'failed', 'message': 'User does not exist or password is incorrect'})), 200
            return make_response(
                jsonify({'status': 'failed',
                         'message': 'Missing or wrong email format or password is less than four characters'})), 200
        return make_response(
            jsonify({'status': 'failed', 'message': 'Content-type must be json'})), 202


# Register classes as views
registration_view = RegisterUser.as_view('register')
login_view = LoginUser.as_view('login')

# Add rules for the api Endpoints
auth.add_url_rule('/auth/register', view_func=registration_view, methods=['POST'])
auth.add_url_rule('/auth/login', view_func=login_view, methods=['POST'])

import uuid
import datetime
from app.main import db, flask_bcrypt
from app.main.model.user import User


def save_new_user(data):
    user = User.objects.filter(email=data['email']).first()
    if not user:
        password = flask_bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=password,
            registered_on=datetime.datetime.utcnow()
        )
        new_user.save()
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.objects.first()


def get_a_user(public_id):
    return User.objects.filter(public_id=public_id).first()

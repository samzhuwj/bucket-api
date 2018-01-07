from app import db
from tests.base import BaseTestCase
from app.models import User
import unittest


class TestUserModel(BaseTestCase):
    """
    Test that the auth token is generated correctly
    """

    def test_encode_user_token(self):
        user = self.create_and_save_user()
        auth_token = self.get_auth_token(user)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_user_token(self):
        user = self.create_and_save_user()
        auth_token = self.get_auth_token(user)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(user.decode_auth_token(auth_token.decode('utf-8')) == 1, msg='The user Id should be 1')

    def create_and_save_user(self):
        user = User(email='example@gmail.com', password='123456')
        db.session.add(user)
        db.session.commit()
        return user

    def get_auth_token(self, user):
        auth_token = user.encode_auth_token(user.id)
        return auth_token


if __name__ == '__main__':
    unittest.main()

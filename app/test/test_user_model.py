import unittest

import datetime

from app.main import db
from app.main.model.user.client import Client
from app.test.base import BaseTestCase


class TestClientModel(BaseTestCase):

    def test_encode_auth_token(self):
        client = Client(
            email='test@test.com',
            password_hash='test',
            created_at=datetime.datetime.utcnow()
        )
        db.session.add(client)
        db.session.commit()
        auth_token = Client.encode_auth_token(client.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        client = Client(
            email='test@test.com',
            password_hash='test',
            created_at=datetime.datetime.utcnow()
        )
        db.session.add(client)
        db.session.commit()
        auth_token = Client.encode_auth_token(client.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(Client.decode_auth_token(
            auth_token.decode("utf-8")) == 1)


if __name__ == '__main__':
    unittest.main()

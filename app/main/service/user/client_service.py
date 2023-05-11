import uuid
import datetime

from app.main import db
from app.main.model.user.client import Client
from typing import Dict, Tuple


def save_new_client(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    import pdb
    pdb.set_trace()

    if client := Client.query.filter_by(email=data['email']).first():
        response_object = {
            'status': 'fail',
            'message': 'Client already exists. Please Log in.',
        }
        return response_object, 409
    else:
        new_client = Client(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            clientname=data['clientname'],
            password=data['password'],
            created_at=datetime.datetime.utcnow()
        )
        save_changes(new_client)
        return generate_token(new_client)


def get_all_clients():
    return Client.query.all()


def get_a_client(public_id):
    return Client.query.filter_by(public_id=public_id).first()


def generate_token(client: Client) -> Tuple[Dict[str, str], int]:
    try:
        # generate the auth token
        auth_token = Client.encode_auth_token(client.client_id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data: Client) -> None:
    db.session.add(data)
    db.session.commit()

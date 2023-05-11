import uuid
import datetime
from app.main.service.user.auth_helper import Auth
from app.main import db
from app.main.model.user.user import User
from typing import Dict, Tuple


def save_new_user(data) -> Tuple[Dict[str, str], int]:
    client_data, _ = Auth.get_logged_in_client(data)
    client = client_data['data']
    if not (
        user := User.query.filter_by(
            user_id=data.json['user_id'], client_id=client['client_id']
        ).first()
    ):
        return _extracted_from_save_new_user_7(data, client)
    response_object = {
        'status': 'fail',
        'message': 'User already exists',
    }
    return response_object, 409


# TODO Rename this here and in `save_new_user`
def _extracted_from_save_new_user_7(data, client):
    data = data.json
    new_user = User(
        user_id=data['user_id'],
        client_id=client['client_id'],
        username=data['username'],
        created_at=datetime.datetime.utcnow()
    )
    import pdb
    pdb.set_trace()
    save_changes(new_user)
    response_object = {
        'status': 'success',
        'message': 'User added successfully',
    }
    return response_object, 201


def get_all_users(data):
    client_data, status = Auth.get_logged_in_client(data)
    if client_data['status'] != 'success':
        return client_data, 409
    client = client_data['data']
    return User.query.filter_by(client_id=client['client_id']).all()


def get_a_user(data):
    client_data, status = Auth.get_logged_in_client(data)
    if client_data['status'] != 'success':
        return data, 409
    client = client_data['data']
    return User.query.filter_by(client_id=client['client_id'], user_id=data.json['user_id']).first()


def save_changes(data: User) -> None:
    db.session.add(data)
    db.session.commit()

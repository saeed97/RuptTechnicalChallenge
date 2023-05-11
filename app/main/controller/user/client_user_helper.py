from app.main.service.user.auth_helper import Auth
from app.main.model.user.user import User
from app.main.model.devices.device import Devices


def is_user_exists(data, user_id):
    client_data, _ = Auth.get_logged_in_client(data)
    client = client_data['data']
    return User.query.filter_by(
        client_id=client['client_id'], user_id=user_id
    ).all()


def is_device_exists(data, user_id, device_id):
    client_data, _ = Auth.get_logged_in_client(data)
    client = client_data['data']
    return Devices.query.filter_by(
        device_id=device_id, user_id=user_id, client_id=client['client_id']
    ).first()

from app.main.model.devices.device import Devices
from app.main.model.user.user import User
from typing import Dict, Tuple
from app.main.service.user.auth_helper import Auth
from app.main import db


def update_user_device_access(data, user_id, device_id) -> Tuple[Dict[str, str], int]:
    """Update user device access"""
    client_data, _ = Auth.get_logged_in_client(data)
    client = client_data['data']

    if device := Devices.query.filter_by(
        device_id=device_id, user_id=user_id, client_id=client['client_id']
    ).first():
        device.access_count += 1
        db.session.commit()
        return {'message': 'Device access count updated successfully'}, 201
    else:
        return {'message': 'Device not found, Please add the device first!'}, 404

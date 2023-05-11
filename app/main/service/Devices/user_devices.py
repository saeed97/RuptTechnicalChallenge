from app.main.model.devices.device import Devices
from typing import Dict, Tuple
from app.main.service.user.auth_helper import Auth
from app.main import db
import sqlalchemy
import logging
import datetime

log = logging.getLogger(__name__)


def get_all_devices(data, user_id) -> Tuple[Dict[str, str], int]:
    """Get all the devices used by a user"""
    client_data, _ = Auth.get_logged_in_client(data)
    client = client_data['data']
    return (
        Devices.query.filter_by(
            user_id=user_id, client_id=client['client_id']
        ).all()
    )


def add_a_new_device(data, user_id):
    """"Add a new device to user devices list"""
    client_data, _ = Auth.get_logged_in_client(data)
    client = client_data['data']
    if device := Devices.query.filter_by(
        user_id=user_id,
        client_id=client['client_id'],
        device_id=data.json['device_id'],
    ).first():
        return {"message": "Device already exists!"}, 409

    return (
        _add_a_new_device(data=data.json, user_id=user_id,
                          client_id=client['client_id'])
    )


def _add_a_new_device(data, user_id, client_id):
    """Add device into a user's table"""
    device_info = Devices(
        device_id=data['device_id'],
        device_type=data['device_type'],
        user_id=user_id,
        client_id=client_id,
        created_at=datetime.datetime.utcnow()

    )
    return save_changes(device_info)


def save_changes(data: Devices) -> None:
    try:
        db.session.add(data)
        db.session.commit()
    except sqlalchemy.exc.DataError or sqlalchemy.exc.InvalidRequestError:
        log.error("ERROR Updating database with viloted data")
        return {"message": "Internal Server Error"}, 505
    return {"message": "Device added Successfully!"}, 201

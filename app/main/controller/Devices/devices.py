from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from app.main.util.dto import Devices
from app.main.service.Devices.user_devices import get_all_devices, add_a_new_device
from app.main.controller.user.client_user_helper import is_user_exists
from typing import Dict, Tuple

api = Devices.api
_device = Devices.devices


@api.route('/users/<string:user_id>')
class DeviceList(Resource):
    @api.doc('list_of_user_devices')
    @token_required
    @api.response(404, 'Invalid request')
    def get(self, user_id):
        """List all user devices"""
        return (
            api.marshal(get_all_devices(
                data=request, user_id=user_id), _device, envelope='data')
            if is_user_exists(request, user_id)
            else (
                {
                    'message': f'The user {user_id} does not exist, please add the user first!',
                    'status': 'failed',
                },
                404,
            )
        )

    @api.expect(_device, validate=True)
    @api.response(201, 'Device added successfully.')
    @api.doc('Add a new device for a user')
    @token_required
    def post(self, user_id) -> Tuple[Dict[str, str], int]:
        """Add a new Device """
        return (
            add_a_new_device(data=request, user_id=user_id)
            if is_user_exists(request, user_id)
            else (
                {
                    'message': f'The user {user_id} does not exist, please add the user first!',
                    'status': 'failed',
                },
                404,
            )
        )

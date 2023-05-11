from flask import request
from flask_restx import Resource


from app.main.util.decorator import token_required
from app.main.service.Access.user_access import update_user_device_access
from app.main.controller.user.client_user_helper import is_user_exists, is_device_exists
from app.main.util.dto import Access
from typing import Dict, Tuple

_device = Access.access
api = Access.api


@api.route('/users/<string:user_id>/devices/<string:device_id>')
class Access(Resource):
    @api.response(201, 'Access Updated successfully.')
    @api.doc('Update a user access of a device')
    @token_required
    def post(self, user_id, device_id) -> Tuple[Dict[str, str], int]:
        """Update access of a device for a user """

        if not is_user_exists(request, user_id=user_id):
            return {
                'message': f'The user {user_id} does not exist, please add the user first!',
                'status': 'failed',
            }, 404

        return (
            update_user_device_access(
                data=request, user_id=user_id, device_id=device_id
            )
            if is_device_exists(request, user_id, device_id=device_id)
            else (
                {
                    'message': f'The device {device_id} does not exist, please add the device for user first!',
                    'status': 'failed',
                },
                404,
            )
        )

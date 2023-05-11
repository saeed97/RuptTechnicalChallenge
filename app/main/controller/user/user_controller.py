from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required, token_required
from app.main.util.dto import UserDto
from app.main.service.user.user_service import save_new_user, get_all_users
from typing import Dict, Tuple

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users(data=request)

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @token_required
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new User """
        return save_new_user(data=request)

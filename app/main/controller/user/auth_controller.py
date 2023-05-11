from flask import request
from flask_restx import Resource

from app.main.service.user.auth_helper import Auth
from app.main.util.dto import AuthDto
from typing import Dict, Tuple

api = AuthDto.api
client_auth = AuthDto.client_auth


@api.route('/login')
class ClientLogin(Resource):
    """
        Client Login Resource
    """
    @api.doc('client login')
    @api.expect(client_auth, validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        # get the post data
        post_data = request.json
        return Auth.login_client(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a client')
    def post(self) -> Tuple[Dict[str, str], int]:
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_client(data=auth_header)

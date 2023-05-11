from flask import request, make_response, render_template
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from app.main.util.dto import ClientDto
from app.main.service.user.client_service import save_new_client, get_all_clients, get_a_client
from typing import Dict, Tuple

api = ClientDto.api
_client = ClientDto.client


@api.route('/')
class ClientList(Resource):
    @api.doc('list_of_registered_clients')
    @admin_token_required
    @api.marshal_list_with(_client, envelope='data')
    def get(self):
        """List all registered clients, only admin"""
        return get_all_clients()

    @api.expect(_client, validate=True)
    @api.response(201, 'Client successfully created.')
    @api.doc('create a new client')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Client """
        data = request.json
        return save_new_client(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Client identifier')
@api.response(404, 'Client not found.')
class Client(Resource):
    @api.doc('get a client')
    @admin_token_required
    @api.marshal_with(_client)
    def get(self, public_id):
        """get a client given its identifier, only admin."""
        if client := get_a_client(public_id):
            return client
        else:
            api.abort(404)

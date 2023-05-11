from flask_restx import Namespace, fields


class ClientDto:
    api = Namespace('Clients', description='Clients related operations')
    client = api.model('client', {
        'email': fields.String(required=True, description='client email address'),
        'clientname': fields.String(required=True, description='client username'),
        'password': fields.String(required=True, description='user password'),
    })


class UserDto:
    api = Namespace('Users', description='Users related operations')
    user = api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'user_id': fields.String(required=True, description='user id Identifier, service consumer')
    })


class AuthDto:
    api = Namespace('Auth', description='Authentication related operations')
    client_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The client password '),
    })


class Devices:
    api = Namespace('Devices', description='Devices related operations')
    devices = api.model('devices', {
        'device_id': fields.String(required=True, description='device id'),
        'device_type': fields.String(required=True, description='device type'),
        'access_count': fields.Integer(required=False, description='device access count')
    })


class Access:
    api = Namespace('Access', description='Devices access related operations')
    access = api.model('access', {
    })

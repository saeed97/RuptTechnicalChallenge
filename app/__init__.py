from flask_restx import Api
from flask import Blueprint
from .main.controller.user.user_controller import api as user_ns
from .main.controller.user.auth_controller import api as auth_ns
from .main.controller.user.client_controller import api as client_ns
from .main.controller.Devices.devices import api as devices_ns
from .main.controller.Access.access import api as access_ns


blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='Technical Challenge for Rupt',
    version='1.0',
    description='User Devices Mointor',
    authorizations=authorizations,
    security='apikey'
)
api.add_namespace(client_ns, path='/api/clients')
api.add_namespace(user_ns, path='/api/users')
api.add_namespace(auth_ns, path='/api')
api.add_namespace(devices_ns, path='/api/devices')
api.add_namespace(access_ns, path='/api/access')

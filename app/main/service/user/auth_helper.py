from app.main.model.user.client import Client
from .blacklist_service import save_token
from typing import Dict, Tuple


class Auth:

    @staticmethod
    def login_client(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the client data
            import pdb
            pdb.set_trace()
            client = Client.query.filter_by(email=data.get('email')).first()
            if client and client.check_password(data.get('password')):
                auth_token = Client.encode_auth_token(client.client_id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_client(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = Client.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_client(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = Client.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                client = Client.query.filter_by(client_id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'client_id': client.client_id,
                        'email': client.email,
                        'admin': client.admin,
                        'created_at': str(client.created_at)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

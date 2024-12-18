from flask import request, jsonify
from app.services.auth_services import AuthService

class AuthController:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service
        
    def generate_auth_token(self):
        token = self.auth_service.generate_token()
        
        if token:
            return jsonify({'token': token}), 200
        return jsonify({'error': 'Error generating token'}), 500

    def authenticate(self):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'error': 'No token provided or invalid format'}), 400

        token = auth_header.split(' ')[1]

        if self.auth_service.authenticate_token(token):
            return jsonify({'message': 'Token is valid'}), 200
        return jsonify({'error': 'Invalid token'}), 401
from flask import request, jsonify
from app.services.auth_services import AuthService
import logging

# Public endpoints dictionary
public_endpoints = {
    'GET': ['/'],
    'POST':['/auth/generateToken']
}

def before_request_middleware():
    if request.method in public_endpoints and request.path in public_endpoints[request.method]:
        return
    
    auth_header = request.headers.get('Authorization', '')
    token = ''
    
    if auth_header.startswith('Bearer '):
        token = auth_header[len('Bearer '):]
        
    auth_service = AuthService()
    
    if not token or not auth_service.authenticate_token(token):
        return jsonify({'message': 'Unauthorized access'}), 401
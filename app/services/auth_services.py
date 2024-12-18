import os
import secrets
import jwt
import logging
from dotenv import load_dotenv, set_key

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

class AuthService:
    def generate_secret_key(self):
        return secrets.token_hex(64)

    def get_secret_key(self):
        secret_key = os.getenv('SECRET_KEY')

        if not secret_key:
            secret_key = self.generate_secret_key()
            logging.debug(f"Generated new SECRET_KEY: {secret_key}")
            set_key('.env', 'SECRET_KEY', secret_key)
            load_dotenv(override=True)

        return secret_key

    def get_stored_token(self):
        return os.getenv('AUTHORIZED_TOKEN')

    def generate_token(self, payload=None):
        try:
            secret_key = self.get_secret_key()

            if payload is None:
                payload = {
                    'sub': '12345678910',
                    'name': 'admin',
                }

            token = jwt.encode(payload, secret_key, algorithm='HS256')
            set_key('.env', 'AUTHORIZED_TOKEN', token)
            logging.debug(f"Generated and stored new token: {token}")

            return token
        except Exception as e:
            logging.error(f"Error generating token: {e}")
            return None

    def authenticate_token(self, token):
        try:
            secret_key = self.get_secret_key()
            decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
            return decoded_token is not None
        except jwt.ExpiredSignatureError:
            logging.error("Token has expired.")
            return False
        except jwt.InvalidTokenError:
            logging.error("Invalid token.")
            return False

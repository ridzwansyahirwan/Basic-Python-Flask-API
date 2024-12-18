from flask import Flask, jsonify
from app.database_config import init_db
from dotenv import load_dotenv
import os
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from app.middleware.auth_middleware import before_request_middleware
from app.routes.auth_routes import auth_bp

load_dotenv()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    
    # Middleware for handling requests
    app.before_request(before_request_middleware)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    @app.route('/', methods=['GET'])
    def home():
        return jsonify({
            'message': 'Welcome to the MAIN API!',
            'available_routes': {
                '/auth': 'Authentication routes',
                '/student': 'Student directory routes',
                '/group': 'Group directory routes',
                '/lecturer': 'Lecturer directory routes'
            }
        })

    DATABASE_URL = os.getenv("MYSQL_DATABASE")
    engine = create_engine(DATABASE_URL)

    with app.app_context():
        init_db()

    return app
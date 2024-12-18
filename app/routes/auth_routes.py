from flask import Blueprint
from app.controllers.auth_controllers import AuthController
from app.services.auth_services import AuthService

auth_bp = Blueprint("auth_bp", __name__)

auth_service = AuthService()
auth_controller = AuthController(auth_service)

@auth_bp.route("/generateToken", methods=["POST"])
def generate_auth_token():
    return auth_controller.generate_auth_token()

@auth_bp.route("/validateToken", methods=["POST"])
def vdalidate_auth_token():
    return auth_controller.authenticate()

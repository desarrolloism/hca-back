from flask import Blueprint, jsonify, request
from app.utils.login import Login

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])

def login():
    data = request.json
    user = Login(data)
    result = user.user_login()
    response = {
        'status': 'ok',
        'data': result
    }
    return jsonify(response)

@login_bp.route('/register', methods=['POST'])

def register():
    data = request.json
    user = Login(data)
    result = user.register()
    response = {
        'status': 'ok',
        'data': result
    }
    return jsonify(response)
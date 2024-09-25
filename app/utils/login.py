from app import db
from flask import request
from app.models.user import User

class Login:
    def __init__(self, dataJson):
        self.dataJson = dataJson

    def user_login(self):
        data = request.json

        email = data.get ('email')
        password = data.get ('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            access_token = user.generate_access_token(identity=user.id)
            return {
                'status': 'ok',
                'message': 'Login successful',
                'access_token': access_token
            }, 200
        else:
            return {
                'status': 'error',
                'message': 'Invalid credentials',
            }, 401
        
    def register(self):
        data = request.json

        dni = data.get ('dni')
        first_name = data.get ('first_name')
        last_name = data.get ('last_name')
        avatar = data.get ('avatar')
        nickname = data.get ('nickname')
        email = data.get ('email')
        password = data.get ('password')
        phone = data.get ('phone')

        user = User(
            dni=dni,
            first_name=first_name,
            last_name=last_name,
            avatar=avatar,
            nickname=nickname,
            email=email,
            password=password,
            phone=phone
        )

        db.session.add(user)
        db.session.commit()

        return {
            'status': 'ok',
            'message': 'User created successfully',
        }, 200
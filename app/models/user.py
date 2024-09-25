from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    
    __tablename__ = 'users'

    id                  = db.Column(db.Integer, primary_key=True)
    dni                 = db.Column(db.String(15), unique=True, nullable=False)
    first_name          = db.Column(db.String(50), nullable=False)
    last_name           = db.Column(db.String(50), nullable=False)
    avatar              = db.Column(db.String(100))  # Puede ser nulo si no se proporciona avatar
    nickname            = db.Column(db.String(50)) # Puede ser nulo si no se proporciona nickname
    email               = db.Column(db.String(150), unique=True, nullable=False)
    password            = db.Column(db.String(255), nullable=False)
    token               = db.Column(db.Text, nullable=True)
    phone               = db.Column(db.String(50), nullable=True)
    is_active           = db.Column(db.Boolean, default=True, nullable=False)
    change_password     = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    def set_password(self, password):
        self.password = generate_password_hash(password) 

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def to_json(self):
        return {
            'id': self.id,
            'dni': self.dni,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'avatar': self.avatar,
            'nickname': self.nickname,
            'email': self.email,
            'password': self.password,
            'token': self.token,
            'phone': self.phone,
            'is_active': self.is_active,
            'change_password': self.change_password,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
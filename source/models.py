import uuid
from datetime import datetime, timedelta

from sqlalchemy.dialects.postgresql import UUID
import jwt
import bcrypt

from . import db, app, API_key


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    is_login = db.Column(db.Boolean())

    def verify_password(self, password):
        # pwhash = bcrypt.hashpw(password.encode(), self.password)
        # return self.password == pwhash
        return password == self.password

    def encode_auth_token(self):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': self.id
        }
        return jwt.encode(
            payload,
            key=API_key,
            algorithm='HS256'
        )

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, API_key, algorithms='HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String())

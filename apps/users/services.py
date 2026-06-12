import bcrypt
from .models import User

class AuthService:

    @staticmethod
    def hash_password(password):

        salt = bcrypt.gensalt()

        return bcrypt.hashpw(
            password.encode('utf-8'),
            salt
        ).decode('utf-8')

    @staticmethod
    def verify_password(password, hashed_password):

        return bcrypt.checkpw(
            password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )

    @staticmethod
    def create_user(data):

        hashed_password = AuthService.hash_password(
            data['password']
        )

        user = User(
            full_name=data['full_name'],
            email=data['email'],
            password=hashed_password
        )

        user.save()

        return user
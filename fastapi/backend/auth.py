from jose import jwt
from environs import Env
from datetime import datetime
from passlib.context import CryptContext


env = Env()
env.read_env()

pwd_hash = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Auth: # noqa D101

    @staticmethod
    def create_token(login, password):
        """Create a new token by user.uuid and date."""
        token = jwt.encode(
            {
                'login': login,
                'password': password,
                'create_time': datetime.utcnow().timetuple()
            },
            env('SECRET'),
            algorithm=env('ALGORITHM')
        )
        return token

    @staticmethod
    def decode_token(token):
        """Decode token from function - create_token."""
        return jwt.decode(token, env('SECRET'), algorithm=env('ALGORITHM'))

    @staticmethod
    def hash_password(password):
        """Hashed password by algorithm."""
        return pwd_hash.hash(password)

    @staticmethod
    def verify_password(password, hash_password):
        """Verify password from function - hash_password."""
        return pwd_hash.verify(password, hash_password)

import os

base_dir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:postgres@localhost/'
database_name = 'api'


class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_strong_key')
    BCRYPT_HASH_PREFIX = 14
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH_TOKEN_EXPIRY_DAYS = 30
    AUTH_TOKEN_EXPIRY_SECONDS = 3000    


class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name    
    BCRYPT_HASH_PREFIX = 4
    AUTH_TOKEN_EXPIRY_DAYS = 0
    AUTH_TOKEN_EXPIRY_SECONDS = 20      


class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + "_test"
    BCRYPT_HASH_PREFIX = 4
    AUTH_TOKEN_EXPIRY_DAYS = 0
    AUTH_TOKEN_EXPIRY_SECONDS = 1    

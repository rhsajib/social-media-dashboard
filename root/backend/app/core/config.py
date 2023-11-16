import os
from dotenv import load_dotenv


# Load environment variables from the .env file in the current directory
load_dotenv()


class BaseConfig:
    def __init__(self):
        ...

class CommonConfig(BaseConfig):
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    DEBUG: str = os.environ.get('DEBUG')
    # ALLOWED_HOSTS: list = os.environ.get('ALLOWED_HOSTS', '').split(',')  # must be list or tuple  # ['host1', 'host2', 'host3']
    ALLOWED_HOSTS: list = ['*']


class DbConfig(BaseConfig):
    DATABASE_NAME: str = os.environ.get('DATABASE_NAME')
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
    HOST: str = os.environ.get('HOST')
    PORT: str = os.environ.get('PORT')

class CoreConfig(DbConfig, CommonConfig):
    pass

config = CoreConfig()
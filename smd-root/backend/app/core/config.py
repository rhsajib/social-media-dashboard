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
    DATABASE_ENGINE: str = os.environ.get('DATABASE_ENGINE')
    POSTGRES_DB: str = os.environ.get('POSTGRES_DB')
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
    # DB_HOST should be set to the service name defined in your docker-compose.yml
    # PG_IMAGE_HOST is for docker image of postgres
    # DB_HOST: str =  os.environ.get('PG_IMAGE_HOST') if os.environ.get('PG_IMAGE_HOST') else os.environ.get('DB_HOST') 
    DB_HOST: str =  os.environ.get('PG_SERVICE', os.environ.get('DB_HOST'))
    DB_PORT: str = os.environ.get('PORT')

class CoreConfig(DbConfig, CommonConfig):
    pass

config = CoreConfig()
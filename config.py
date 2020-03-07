import os
from dotenv import load_dotenv
from sqlalchemy.engine.url import URL

dotenv_path = './.env'
load_dotenv(dotenv_path)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

GUNICORN_WORKERS = os.environ['GUNICORN_WORKERS']
GUNICORN_WEBSERVER_WORKER_TYPE = os.getenv('GUNICORN_WEBSERVER_WORKER_TYPE', 'gevent')
GUNICORN_WEBSERVER_TIMEOUT = os.environ['GUNICORN_WEBSERVER_TIMEOUT']

FLASK_WEBSERVER_ADDRESS = os.environ['FLASK_WEBSERVER_ADDRESS']
FLASK_WEBSERVER_PORT = os.environ['FLASK_WEBSERVER_PORT']


SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = int(os.environ['SQLALCHEMY_POOL_SIZE'])
SQLALCHEMY_POOL_TIMEOUT = int(os.environ['SQLALCHEMY_POOL_TIMEOUT'])
SQLALCHEMY_POOL_RECYCLE = int(os.environ['SQLALCHEMY_POOL_RECYCLE'])
SQLALCHEMY_MAX_OVERFLOW = int(os.environ['SQLALCHEMY_MAX_OVERFLOW'])


def get_database_url():
    driver = os.getenv('APP_DB_DRIVER', 'postgresql')
    username = os.getenv('APP_DB_USER', 'app')
    password = os.getenv('APP_DB_PASS', 'password')
    address = os.getenv('APP_DB_HOST', 'localhost')
    port = os.getenv('APP_DB_PORT', '5432')
    database = os.getenv('APP_DB_DATABASE', 'app')
    return str(
        URL(drivername=driver, username=username, password=password, host=address,
            port=port, database=database))


SQLALCHEMY_DATABASE_URI = get_database_url()
DEBUG = False

FLASK_USE_RELOAD = True

LOG_FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
LOG_LEVEL = 'DEBUG'
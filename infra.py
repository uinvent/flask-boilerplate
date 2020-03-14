import os
from dotenv import load_dotenv
import logging
from src.models import migrate, db
from flask import Flask

ENV_FILE_PATH = './.env'


app = Flask(__name__)

dotenv_path = ENV_FILE_PATH
# Load .env file and if .env file is not found then will use system environment variables
load_dotenv(dotenv_path, override=True)
app.config.from_envvar('FLASK_CONFIG_FILE_PATH')

conf = app.config

from src.apis import register_api
register_api()

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

db.init_app(app)
migrate.init_app(app, db, directory=os.environ['MIGRATION_FOLDER_PATH'])
logging.basicConfig(format=conf.get('LOG_FORMAT'))
logging.getLogger().setLevel(conf.get('LOG_LEVEL'))
"""
initialization of model classes and their migrations
"""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

from .address import *
from .person import *


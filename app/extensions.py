# -*- coding: utf-8 -*-

from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

db = SQLAlchemy()
migrate = Migrate()
api = Api(prefix="/api")
redis = FlaskRedis()

# -*- coding: utf-8 -*-

import logging

from flask import Flask

from app import resources
from app.extensions import api, db, migrate, redis
from app.admin import routers


def create_app(object_name):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object("app.configs.%s.Config" % object_name)

    app.logger.setLevel(logging.INFO)

    resources.init(api)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    redis.init_app(app)
    routers.init_app(app)

    return app

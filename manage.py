# -*- coding: utf-8 -*-

import os

from app.models import Base

from flask.cli import load_dotenv

from app import create_app
from commands import create_admin

load_dotenv()
app = create_app(os.getenv("FLASK_ENV"))
app.cli.add_command(create_admin)


@app.after_request
def after_reqeust_callback(response):
    """请求结束回调函数"""

    # 跨域配置
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization,X-Requested-With,Content-Type'

    return response

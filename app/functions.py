# -*- coding: utf-8 -*-

import datetime
import importlib
import os
import pkgutil
import random
import string
from _sha1 import sha1
from decimal import Decimal
from functools import wraps
from inspect import getmembers, isfunction

from flask import g, redirect, request, session
from flask_restful import abort

from app.extensions import db, redis
from json import loads
import hashlib
from app.constants import TOKEN_EXPIRES
import re


def get_sub_modules(module_name):
    """获取子模块迭代器"""

    package = importlib.import_module(module_name)
    for module in pkgutil.iter_modules(package.__path__):
        yield importlib.import_module("%s.%s" % (module_name, module[1]))


def get_module_functions(module_name):
    """获取模块下所有函数的迭代器"""

    module = importlib.import_module(module_name)
    for member in getmembers(module, isfunction):
        yield member


def get_endpoint():
    """获取当前的endpoint"""

    return request.endpoint.replace("_", ".")


def login_required(admin=True):
    """登录认证装饰器"""

    def _login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            from app.services import user_srv

            if "user_id" not in session:
                return redirect(url_for("auth.login", next=get_endpoint()))

            user = user_srv.get(session["user_id"])
            if not user:
                session.clear()
                return redirect(url_for("auth.login"))

            if admin and not user.admin:
                return redirect(url_for("index.index"))

            g.user = user

            result = f(*args, **kwargs)
            db.session.commit()

            return result

        return decorated_function

    return _login_required


def get_token():
    """获取token值"""

    auth = request.headers.get("Authorization")

    if not auth:
        return False

    if auth.startswith("Bearer "):
        return auth.split(" ")[1]

    return False


def api_required(must=True):
    """登录认证装饰器"""

    def _api_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            from app.services import user_srv

            token = get_token()
            if not token:
                if must:
                    abort(401, msg="请重新登录")
                else:
                    return f(*args, **kwargs)

            key = "Token:%s" % token
            user_id = redis.get(key)
            if not user_id:
                abort(401, msg='请重新登录')

            user = user_srv.get(int(user_id))
            if not user:
                redis.delete(key)
                abort(401)

            g.user = user

            result = f(*args, **kwargs)
            db.session.commit()

            return result

        return decorated_function

    return _api_required


def is_login():
    """判断是否登陆"""

    return "user" in g


def generate_captcha():
    """生成验证码"""

    random_digits = random.sample(string.digits, 6)
    random_list = random_digits

    random.shuffle(random_list)

    return "".join(random_list)


def camel_to_underline(camel_format):
    """驼峰命名格式转下划线命名格式"""

    underline_format = ''
    if isinstance(camel_format, str):
        for _s_ in camel_format:
            underline_format += _s_ if _s_.islower() else '_' + _s_.lower()
    return underline_format.lstrip("_")


def underline_to_camel(underline_format):
    """下划线命名格式驼峰命名格式"""

    camel_format = ''
    if isinstance(underline_format, str):
        for _s_ in underline_format.split('_'):
            camel_format += _s_.capitalize()
    return camel_format


def time_format(timestamp):
    """时间戳转datetime"""

    return datetime.datetime.fromtimestamp(int(timestamp))


def generate_unique_code():
    return datetime.datetime.today().strftime('%Y%m%d') + ''.join(random.sample(string.digits, 8))


def encode_decimal(o):
    if isinstance(o, Decimal):
        return float(round(o, 8))
    raise TypeError(repr(o) + " is not JSON serializable")


def generate_token():
    return sha1(os.urandom(24)).hexdigest()


def generate_and_save_token(user_id):
    token = generate_token()
    key = "Token:%s" % token
    redis.set(key, user_id)
    redis.expire(key, TOKEN_EXPIRES)
    return token


def parse_json(val):
    try:
        datas = loads(val)
        return datas
    except ValueError:
        return False


def password_hash(password):
    h = hashlib.sha256()
    h.update(bytes(password, encoding='utf-8'))
    return h.hexdigest()


def is_email(email):
    ex_email = re.compile(r'^[\w][a-zA-Z1-9.]{4,19}@[a-zA-Z0-9]{2,3}.[com|gov|net]')
    result = ex_email.match(email)
    return result

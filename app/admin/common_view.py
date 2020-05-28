from flask.views import MethodView
from app.extensions import db
from functools import wraps
from flask import session, redirect, url_for, g
from app.functions import get_endpoint
from app.services import admin_srv


class CommonView(MethodView):

    @staticmethod
    def login_required():
        """登录认证装饰器"""

        def _login_required(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                if "admin_id" not in session:
                    return redirect(url_for("admin.login", next=get_endpoint()))

                admin = admin_srv.get(session['admin_id'])
                g.admin = admin
                result = f(*args, **kwargs)
                db.session.commit()
                return result

            return decorated_function

        return _login_required

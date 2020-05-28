from .login.views import LoginView
from flask.blueprints import Blueprint

bp = Blueprint('admin', __name__, url_prefix="/admin")
bp.add_url_rule('/login', view_func=LoginView.as_view('login'), methods=['get', 'post'])


def init_app(app):
    app.register_blueprint(bp)

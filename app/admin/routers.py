from .login.views import LoginView
from .index.views import IndexView

from flask.blueprints import Blueprint

bp = Blueprint('admin', __name__, url_prefix="/admin")
bp.add_url_rule('/login', view_func=LoginView.as_view('login'), methods=['get', 'post'])
bp.add_url_rule('/index', view_func=IndexView.as_view('index'), methods=['get'])


def init_app(app):
    app.register_blueprint(bp)

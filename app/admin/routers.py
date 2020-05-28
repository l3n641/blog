from .login.views import LoginView
from .index.views import IndexView, ProfileView, RestPasswordView

from flask.blueprints import Blueprint

bp = Blueprint('admin', __name__, url_prefix="/admin")
bp.add_url_rule('/login', view_func=LoginView.as_view('login'), methods=['get', 'post'])
bp.add_url_rule('/index', view_func=IndexView.as_view('index'), methods=['get'])
bp.add_url_rule('/profile', view_func=ProfileView.as_view('profile'), methods=['get'])
bp.add_url_rule('/repassword', view_func=RestPasswordView.as_view('repassword'), methods=['get', 'post'])


def init_app(app):
    app.register_blueprint(bp)

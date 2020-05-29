from .login.views import LoginView
from .index.views import IndexView, ProfileView, RestPasswordView
from .post.views import PostView, PostListView, PostSeachView, PostDetailView
from .tag.views import TagView

from flask.blueprints import Blueprint

bp = Blueprint('admin', __name__, url_prefix="/admin")
bp.add_url_rule('/login', view_func=LoginView.as_view('login'), methods=['get', 'post'])
bp.add_url_rule('/index', view_func=IndexView.as_view('index'), methods=['get'])
bp.add_url_rule('/profile', view_func=ProfileView.as_view('profile'), methods=['get'])
bp.add_url_rule('/repassword', view_func=RestPasswordView.as_view('repassword'), methods=['get', 'post'])
bp.add_url_rule('/post', view_func=PostView.as_view('post'), methods=['get', 'post'])
bp.add_url_rule('/tag', view_func=TagView.as_view('tag'), methods=['get', 'post'])
bp.add_url_rule('/post_list', view_func=PostListView.as_view('post_list'), methods=['get', 'post'])
bp.add_url_rule('/post_search', view_func=PostSeachView.as_view('post_search'), methods=['post'])
bp.add_url_rule('/post_detail/<int:_id>', view_func=PostDetailView.as_view('post_detail'), methods=['get', 'post'])


def init_app(app):
    app.register_blueprint(bp)

from app.admin.common_view import CommonView
from flask import render_template, g, request
from .forms import PostForm
from flask_restful import reqparse, marshal, fields
from app.extensions import editor
from app.services import post_srv, tag_srv
from app.constants import DEFAULT_PAGE


class PostView(CommonView):
    """
    发表新帖子
    """

    def __init__(self, *args):
        super().__init__()
        self.form = PostForm()

    @CommonView.login_required()
    def get(self):
        return render_template("admin/posts.html", form=self.form, editor=editor)

    @CommonView.login_required()
    def post(self):
        tag_ids = [tag.id for tag in tag_srv.get_all()]
        parse = reqparse.RequestParser()
        parse.add_argument("title", type=str, required=True, help="title必须存在")
        parse.add_argument("content", type=str, required=True, help="content必须存在")
        parse.add_argument("tags", choices=tag_ids, type=int, required=True, help="tags错误", action='append',
                           location=["json", "form"])
        data = parse.parse_args()
        _id = post_srv.save(author_id=g.admin.id, **data)

        if _id:
            return {'code': '201', 'data': {"id": _id}}, 201
        else:
            return self._service.get_error(), 400


class PostListView(CommonView):
    """
    post列表
    """

    def get(self):
        page = int(request.args.get('page') or DEFAULT_PAGE)
        posts = post_srv.get_list(page=page)
        return render_template("admin/post_list.html", posts=posts)

    @CommonView.login_required()
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("id", type=int, required=True, help="post_id必须存在", action='append',
                           location=["json", "form"])
        data = parse.parse_args()

        if post_srv.delete(data):
            return '', 204
        else:
            return self._service.get_error(), 400


class PostSeachView(CommonView):
    """
    posts 搜索
    """

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, required=True, help="标题必须存在")
        form_data = parser.parse_args()
        posts = post_srv.search('title', form_data.get("title"))

        data = marshal(posts, {
            "id": fields.Integer,
            "title": fields.String,
            "content": fields.String,
            "author_id": fields.Integer(attribute="author.id"),
            "username": fields.String(attribute="author.username"),
            "email": fields.String(attribute="author.email"),
            "create_time": fields.DateTime("iso8601"),
        })

        return {"code": 200, "data": data}

from app.admin.common_view import CommonView
from flask import render_template, g
from .forms import PostForm
from flask_restful import reqparse, Resource
from app.extensions import editor
from app.services import post_srv, tag_srv


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




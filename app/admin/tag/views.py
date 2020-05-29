from app.admin.common_view import CommonView
from flask import render_template, jsonify
from .forms import TagForm
from app.services import tag_srv
from flask_restful import marshal, fields, reqparse


class TagView(CommonView):
    """
    tags
    """

    def __init__(self, *args):
        super().__init__()
        self.form = TagForm()

    @CommonView.login_required()
    def get(self):
        """
        获取全部tag
        """
        tags = tag_srv.get_all()
        return {
            "code": 200,
            "tags": marshal(tags, {'id': fields.Integer, "name": fields.String})
        }

    @CommonView.login_required()
    def post(self):
        """
        添加tag
        """
        parser = reqparse.RequestParser()
        parser.add_argument('tag', type=tag_srv.is_tag_unique, help="tag名称必须存在", required=True,
                            location=["form", "json"])
        form_data = parser.parse_args(strict=True)
        tag_id = tag_srv.save(**{"name": form_data.get("tag")})
        response = {
            "code": 200,
            "data": {
                "id": tag_id,
                "name": self.form.data.get("tag")
            }
        }

        return jsonify(response)


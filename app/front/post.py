from app.resources.common import Common
from flask_restful import marshal, fields

tags_fields = {
    "id": fields.Integer,
    "name": fields.String
}

posts_fields = {
    "id": fields.Integer,
    "create_time": fields.String,
    "title": fields.String,
    "content": fields.String,
    'tags': fields.List(fields.Nested(tags_fields), attribute='tags'),
    'post_views': fields.Integer(attribute="post_views.amount")
}


class Post(Common):
    def get(self, id=None):
        self._fields = posts_fields
        if id:
            self._service.update_read(id)
        return self._get(_id=id)

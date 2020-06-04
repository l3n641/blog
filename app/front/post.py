from app.resources.common import Common
from flask_restful import marshal, fields
tags_fields={
    "id":fields.Integer,
    "name":fields.String
}

posts_fields = {
    "id": fields.Integer,
    "title":fields.String,
    "content":fields.String,
    'tags': fields.List(fields.Nested(tags_fields), attribute='tags')
}


class Post(Common):
    def get(self):
        self._fields = posts_fields
        print(self._service)
        return self._get()

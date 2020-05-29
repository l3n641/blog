from .common import CommonService


class PostService(CommonService):
    def save(self, **kwargs):
        from app.services import tag_srv
        tags = tag_srv.get(kwargs.get("tags"))
        kwargs['tags'] = tags
        self.columns.append('tags')
        return super(PostService, self).save(**kwargs)

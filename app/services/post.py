from .common import CommonService
from app.models import PostViews


class PostService(CommonService):
    def save(self, **kwargs):
        from app.services import tag_srv
        tags = tag_srv.get(kwargs.get("tags"))
        kwargs['tags'] = tags
        kwargs['post_views'] = PostViews(amount=0)
        self.columns.append('tags')
        self.columns.append('post_views')
        return super(PostService, self).save(**kwargs)

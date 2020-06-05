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

    def update_read(self, post_id):
        """
        更新阅读量
        """
        from app.models import PostViews
        from app.extensions import db

        data = PostViews.query.filter(PostViews.post_id == post_id).with_for_update().one()
        data.amount = data.amount + 1
        db.session.add(data)
        db.session.commit()

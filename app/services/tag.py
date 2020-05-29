from .common import CommonService


class TagService(CommonService):

    def is_tag_unique(self, tag):
        data = self.get_first({"name": tag})
        if data:
            raise ValueError("该标签已经存在")
        return tag

# -*- coding: utf-8 -*-

from .admin import AdminService
from .tag import TagService
from .post import PostService
from .category import CategoryService


admin_srv = AdminService()
tag_srv = TagService()
post_srv = PostService()
category_srv=CategoryService()
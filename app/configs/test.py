# -*- coding: utf-8 -*-

from datetime import timedelta
from .common import Common


class Config(Common):
    TESTING = True
    TRANS_COMMENT = "automation[test]"


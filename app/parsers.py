# -*- coding: utf-8 -*-

from flask_restful import reqparse

from app.functions import time_format
from app.constants import DEFAULT_PAGE, DEFAULT_PAGE_SIZE

# 分页解析器
page_parser = reqparse.RequestParser()
page_parser.add_argument(
    'page',
    type=int,
    default=DEFAULT_PAGE,
    required=False,
    location=['args'],
    help='page must be a number',
)
page_parser.add_argument(
    'page_size',
    type=int,
    default=DEFAULT_PAGE_SIZE,
    required=False,
    location=['args'],
    help='page_size must be a number',
)

time_range_parser = reqparse.RequestParser()
time_range_parser.add_argument(
    'start_time',
    type=time_format,
    required=False,
    location=['args'],
)
time_range_parser.add_argument(
    'end_time',
    type=time_format,
    required=False,
    location=['args'],
)

create_time_parser = reqparse.RequestParser()
create_time_parser.add_argument(
    'create_time_start',
    type=time_format,
    required=False,
    location=['args'],
)
create_time_parser.add_argument(
    'create_time_end',
    type=time_format,
    required=False,
    location=['args'],
)
order_parser = reqparse.RequestParser()
order_parser.add_argument('order_field', type=str, required=False, default=None, location=["args"])
order_parser.add_argument('order_type', type=str, required=False, default="desc", location=["args"])

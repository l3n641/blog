# -*- coding: utf-8 -*-

import importlib

from flask import abort, g
from flask_restful import Resource, marshal

from app.functions import camel_to_underline
from app.parsers import page_parser, create_time_parser


class Common(Resource):
    _service = None
    _get_parser = None
    _post_parser = None
    _put_parser = None
    _fields = None
    _list_fields = None
    _time_filter = False

    def __init__(self):
        if not self._service:
            service_name = "%s_srv" % camel_to_underline(self.__class__.__name__)
            models = importlib.import_module("app.services")
            self._service = getattr(models, service_name)
        super(Common, self).__init__()

    def _get(self, _id=None, where=None):
        if not self._fields:
            abort(404)

        if _id:
            data = self._service.get(_id)
            if not data:
                abort(404)
            return marshal(data, self._fields)
        if not where:
            where = {}
        if self._get_parser:
            where.update(self._get_parser.parse_args())
            where = {k: v for k, v in where.items() if v}

        if "user_id" in self._service.columns:
            where["user_id"] = g.user.id

        if self._time_filter:
            time_range_args = create_time_parser.parse_args()
            start_time = time_range_args.get("create_time_start")
            end_time = time_range_args.get("create_time_end")
            if start_time or end_time:
                where['create_time'] = {}
            if start_time:
                where["create_time"]['gt'] = start_time
            if end_time:
                where["create_time"]['lt'] = end_time

        page_args = page_parser.parse_args()
        data = self._service.get_list(where=where,
                                      page=page_args['page'],
                                      page_size=page_args['page_size'])

        self._list_fields = self._list_fields or self._fields
        return {
            'data': marshal(data.items, self._list_fields),
            'total': data.total,
        }

    def _delete(self, _id=None):
        if not _id:
            abort(404)

        if self._service.delete(_id):
            return '', 204
        else:
            return self._service.get_error(), 400

    def _post(self):
        if not self._post_parser:
            abort(404)

        post_args = self._post_parser.parse_args(strict=True)
        _id = self._service.save(**post_args)

        if _id:
            return _id, 201
        else:
            return self._service.get_error(), 400

    def _put(self, _id=None):
        if not self._put_parser or not _id:
            abort(404)

        put_args = self._put_parser.parse_args(strict=True)
        put_args = {k: v for k, v in put_args.items() if v}
        result_id = self._service.save(id=_id, **put_args)

        if result_id:
            return self._get(result_id)
        else:
            return self._service.get_error(), 400

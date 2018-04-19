#!/usr/bin/env python
# coding: utf-8
# author: LiuYue
# e-mail: liuyue@mobike.com
# blog  : http://liuyue.club/
# Pw @ 2018/4/19 下午6:33


import json


class MyModel(object):
    """
    My Own Model
    """
    __tablename__ = None

    def __repr__(self):
        return '<Role %r>' % self.__tablename__

    def to_json(self):
        json_data = dict()
        for attr in self.__dict__:
            if not attr.startswith("_"):
                json_data[attr] = self.__getattribute__(attr)
        return json.dumps(json_data)

    def from_json(self, json_data):
        json_data = json.loads(json_data)
        for keys in json_data:
            self.__setattr__(keys, json_data.get(keys, None))

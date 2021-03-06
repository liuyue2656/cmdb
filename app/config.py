#!/usr/bin/env python
# coding: utf-8
# author: LiuYue
# e-mail: liuyue@mobike.com
# blog  : http://liuyue.club/
# Pw @ 2018/4/18 下午6:55

import os
import datetime
import logging


basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(object):
    ENV = "development"
    DEBUG = True
    SECRET_KEY = "DtPrdVSm22gWpstYbT9ti9b6TvhbdqIr"
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/lcmd?charset=utf8'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_EXPIRE_ON_COMMIT = True
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=60)
    LOG_LEVEL = logging.DEBUG
    LOG_FILE = os.path.join(basedir, "logs/access.log")

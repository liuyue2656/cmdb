#!/usr/bin/env python
# coding: utf-8
# author: LiuYue
# e-mail: liuyue@mobike.com
# blog  : http://liuyue.club/
# Pw @ 2018/4/19 下午6:31


from . import dashboard


@dashboard.route("/")
def dashboard_root():
    return "Hello, World!"

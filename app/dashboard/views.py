#!/usr/bin/env python
# coding: utf-8
# author: LiuYue
# e-mail: liuyue@mobike.com
# blog  : http://liuyue.club/
# Pw @ 2018/4/19 下午6:31


from . import dashboard
from flask import render_template
from flask_login import login_required


@dashboard.route("/")
@login_required
def dashboard_root():
    return render_template("dashboard/dashboard_root.html")

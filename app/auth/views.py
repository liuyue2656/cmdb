#!/usr/bin/env python
# coding: utf-8
# author: LiuYue
# e-mail: liuyue@mobike.com
# blog  : http://liuyue.club/
# Pw @ 2018/4/19 下午3:39


from . import auth
from flask import redirect, url_for, render_template


@auth.route("/")
def rewrite_root():
    return redirect(url_for(".login_page"))


@auth.route("/login/")
def login_page():

    return render_template("auth/login.html")

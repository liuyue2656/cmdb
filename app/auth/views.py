#!/usr/bin/env python
# coding: utf-8
# author: LiuYue
# e-mail: liuyue@mobike.com
# blog  : http://liuyue.club/
# Pw @ 2018/4/19 下午3:39


from datetime import datetime
from . import auth
from flask import redirect, url_for, render_template, flash, session, request
from flask_login import current_user, login_user
from forms import LoginForm
from app.models.user import User


@auth.route("/")
def rewrite_root():
    return redirect(url_for(".login_page"))


@auth.route("/login/")
def login_page():
    # NOTE: 登录视图函数
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user.check_password(form.password.data):
            flash(u"密码错误")
            return redirect(url_for(".login_page"))
        else:
            login_user(user, form.remember_me.data)
            user.last = datetime.today()
            session.permanent = True
            return redirect(
                request.args.get("next") or url_for("dashboard.index")
            )
            # current_user.menu = current_user.generate_menu()
    return render_template("auth/login.html", form=form)

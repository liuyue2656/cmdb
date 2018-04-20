#!/usr/bin/env python
# coding: utf-8
# author: LiuYue
# e-mail: liuyue@mobike.com
# blog  : http://liuyue.club/
# Pw @ 2018/4/19 下午3:45


from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField, ValidationError,
    SelectField
)
from wtforms.validators import Required, Length
from app.models.user import User


class LoginForm(FlaskForm):
    u"""
    登陆表单
    """
    email = StringField(u"Email", validators=[Required(), Length(10, 64)])
    password = PasswordField(u"密码", validators=[Required()])
    remember_me = BooleanField(u"记住我")
    submit = SubmitField(u"确认登录")

    def validate_email(self, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError(u"用户不存在")
#!/usr/bin/env python
# coding: utf-8
# author: LiuYue
# e-mail: liuyue@mobike.com
# blog  : http://liuyue.club/
# Pw @ 2018/4/19 下午3:38


from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import json
import collections
from app.models.base import MyModel


class User(UserMixin, db.Model):
    u"""
    用户信息
    """
    __tablename__ = "user_user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username = db.Column(db.String(64), nullable=False)
    tel_num = db.Column(db.String(11))
    status = db.Column(db.Boolean, nullable=False, default=True)
    _password = db.Column(db.String(128), nullable=False)
    last = db.Column(db.DateTime)
    own_menu = db.String(2048)
    logs = db.relationship("Log", backref="user")
    # roles = db.relationship("Role", secondary=user_role,
    #                         backref=db.backref("user", lazy="dynamic"))

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    def can(self, permission):
        # NOTE: 验证权限
        if permission in [permission.name for role in self.roles
                                          for permission in role.permissions]:
            return True
        else:
            return False

    def generate_menu(self):
        # NOTE: 生成用户个性化菜单
        menu_dict = collections.OrderedDict()
        child_menu = set()
        for role in self.roles:
            for permission in role.permissions:
                child_menu.update(permission.menus)
        parent_menu = child_menu & set(Menu.query.filter_by(pid=0).all())
        child_menu = child_menu - parent_menu
        parent_menu = sorted(parent_menu, key=lambda key: key.display_order)
        for menu in parent_menu:
            if menu.url:
                menu_dict[menu.title] = menu.url
            else:
                menu_dict[menu.title] = collections.OrderedDict()
                _menu = [m for m in child_menu if m.pid == menu.id]
                _menu = sorted(_menu, key=lambda key: key.display_order)
                for c_menu in _menu:
                    menu_dict[menu.title][c_menu.title] = c_menu.url
        return json.dumps(menu_dict)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model, MyModel):
    u"""
    角色表
    """
    __tablename__ = "user_role"
    name = db.Column(db.String(64), unique=True, nullable=False)
    display_name = db.Column(db.String(64), unique=True, nullable=False)
    permission = db.Column(db.Ingeter)
    status = db.Column(db.Boolean, nullable=False, default=True)


class Menu(db.Model, MyModel):
    u"""
    菜单表
    """
    __tablename__ = "user_menu"
    name = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(128), unique=True, nullable=False)
    # NOTE 父目录ID，0为顶级目录
    pid = db.Column(db.Integer, nullable=False, default=0)
    url = db.Column(db.String(256))
    display_order = db.Column(db.Integer, nullable=False)
    logs = db.relationship("Log", backref="menu")

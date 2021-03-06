#!/usr/bin/env python
# coding: utf-8
# author: LiuYue
# e-mail: liuyue@mobike.com
# blog  : http://liuyue.club/
# Pw @ 2018/4/18 下午3:17

from app import create_app, db
from app.models.user import User
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()

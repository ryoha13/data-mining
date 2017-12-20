#! -*- coding:utf-8 -*-

import pymysql
from configs import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_moment import Moment
from flask_bootstrap import Bootstrap


pymysql.install_as_MySQLdb()


bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])     # 调用Flask的from_object方法引入配置，配置再初始化flask实例
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


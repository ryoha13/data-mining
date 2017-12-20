#! -*- coding:utf-8 -*-


class Config:
    SECRET_KEY = 'cyukurena13'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # mail info
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'ryoha13@163.com'
    MAIL_PASSWORD = 'tsumugihs13'
    MAIL_ADMIN = 'ryoha13@163.com'

    # blog info

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:2080kk757@localhost:3306/dev_p?charset=utf8'


class ProConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:2080kk757@localhost:3306/pro?charset=utf8'


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:2080kk757@localhost:3306/test?charset=utf8'


config = {
    'dev': DevConfig,
    'pro': ProConfig,
    'test': TestConfig,
    'default': DevConfig
}
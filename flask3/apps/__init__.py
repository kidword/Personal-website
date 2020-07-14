# -*- coding: utf-8 -*-
# 创建管理所有项目逻辑代码的包apps
from flask import Flask
from flask_cors import *


def register_cms_bp(app):
    from apps.admin import cms_bp
    # 将蓝图注册到app上
    app.register_blueprint(cms_bp)


def get_cms_app(config_obj: str):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    # 增加app系统配置
    app.config.from_object(config_obj)
    register_cms_bp(app)
    return app

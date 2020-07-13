# !/bin/bash
# -*- coding: utf-8 -*-

from flask import Blueprint

# 实例化蓝图对象
cms_bp = Blueprint('cms', __name__)

from . import user_view
from . import info
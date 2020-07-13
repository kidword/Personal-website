# !/bin/bash
# -*- coding: utf-8 -*-

from . import cms_bp


@cms_bp.route('/')
def index():
    return "hello world"


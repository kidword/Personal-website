# !/bin/bash
# -*- coding: utf-8 -*-

from . import cms_bp


@cms_bp.route('/atlas')
def get_atlas():
    return "hello atlas"

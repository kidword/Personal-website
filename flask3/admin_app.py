# !/bin/bash
# -*- coding: utf-8 -*-

from apps import get_cms_app

cms_app = get_cms_app('apps.config.CMSDevConfig')

if __name__ == '__main__':
    cms_app.run(port=7000)

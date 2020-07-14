# !/bin/bash
# -*- coding: utf-8 -*-
import json
from flask import request
from . import cms_bp
from flask import jsonify


@cms_bp.route('/')
def index():
    return "hello world"


@cms_bp.route('/login', methods=['GET', 'POST'])
def UserInfo():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            print(username, password)
        return jsonify(
            {'data': {'msg': 'success', 'token': '123'},
             'code': 20000}
        )


@cms_bp.route('/userinfo', methods=['GET', 'POST'])
def Userget():
    if request.method == 'GET':
        return jsonify(
            {'data': {'msg': 'success', 'token': '123'},
             'code': 20000}
        )

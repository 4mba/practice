# -*- coding: utf-8 -*-
"""
photolog-ui
~~~~~~~~~~~~~~~~~~

플라스크 웹 어플리케이션에서 보여지는 layout을 확인해보기 위한 임시 페이

:copyright: (c) 2013 by Jou Sung Shik
:license: BSD, see LICENSE for more details.
"""

from flask import Flask, request, session, g, redirect, url_for, abort, \
	 render_template, flash, _app_ctx_stack


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('main.html')


@app.route('/user/login')
def index():
    return render_template('login.html')

@app.route('/user/register')
def index():
    return render_template('register.html')


@app.route('/layout')
def index():
    return render_template('layout.html')


@app.route('/user/register')
def index():
    return render_template('layout.html')

@app.route('/photo/upload')
def index():
    return render_template('layout.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
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


@app.route('/user/login')
def login():
    return render_template('login.html')


@app.route('/user/regist')
def parent():
    return render_template('regist.html')

@app.route('/photo/upload')
def upload():
    return render_template('upload.html')


@app.route('/photo/entry/all')
def entry_all():
    return render_template('entry_all.html')


@app.route('/photo/entry/<id>')
def entry():
    return render_template('upload.html')




def not_found(error):
#     print "404 Page not found"
    return render_template('404.html')

def server_error(error):
    print "500 Server Error : %s" % error
    return render_template('500.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

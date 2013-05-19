#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, request, session, g, redirect, \
                  url_for, abort, render_template, flash, \
                  jsonify

import Project , json , Config
import logging 
from logging import handlers

# Flask Application 선언
app = Flask(__name__)
app.config.from_object('Config.DevelopmentConfig')

log = logging.getLogger('MyLogger')
log.setLevel(Config.DevelopmentConfig.LOGLEVEL)

# 로그 로테이션을 사용
fileh = handlers.RotatingFileHandler(Config.DevelopmentConfig.LOGFILE, maxBytes=1024000, backupCount=5) 
lformat = logging.Formatter("%(asctime)s [%(levelname)s] - %(message)s")
fileh.setFormatter(lformat)
log.addHandler(fileh)
 


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/search/<oss_name>/<page_num>')
def search(oss_name, page_num):
    prj = Project.Project(oss_name)
    projects = prj.get_project(page_num)
    result = json.dumps(projects)
    
    # debug 모드일때만 로그 기록 
    log.debug(oss_name +":"+ page_num)
    log.debug(result)

    return result




if __name__ == '__main__':
    app.run()


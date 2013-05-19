# -*- coding: utf-8 -*-

import logging

class Config(object):
    """ APP의 설정 정보들을 가지고 있는 클래스
    """ 
 
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    LOGLEVEL = logging.DEBUG
    LOGFILE = 'log/osslh.log'

class ProductionConfig(Config):
    """ Production 단계에서 적용되는 설정 
    """
    DATABASE_URI = 'mysql://user@localhost/foo'
    LOGLEVEL = logging.INFO
    LOGFILE = 'log/osslh.log'

class DevelopmentConfig(Config):
    """ Development 단계에서 적용되는 설정 
    """
    DEBUG = True
    LOGLEVEL = logging.DEBUG
    LOGFILE = 'log/osslh.log'

class TestingConfig(Config):
    """ Testing 단계에서 적용되는 설정 
    """
    TESTING = True
    LOGLEVEL = logging.DEBUG
    LOGFILE = 'log/osslh.log'



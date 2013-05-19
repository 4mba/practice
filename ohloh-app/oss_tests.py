#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    oss.py Tests
    ~~~~~~~~~~~~

"""
import oss
import json
import unittest
import inspect


class OssTestCase(unittest.TestCase):

    def setUp(self):
        """테스트 클라이언트 생성 / 기타 초기화 작업 """
        oss.app.config['TESTING'] = True
        self.app = oss.app.test_client()

    def tearDown(self):
        """테스트 데이터 삭제.."""


    def search(self, oss_name, page_num):
        """ 오픈소스 검색 입력 테스트 /GET , /search/jquery/1 """
        return self.app.get('/search/'+oss_name+'/'+page_num, follow_redirects=True)


    # testing functions


    def test_search(self):
        """ 오픈소스 검색 입력 테스트 /GET , /search/jquery/1 """
        rv = self.search('jquery','1')
#        print rv
        assert json.loads(rv.data) , 'TEST SUCCESS!' 


if __name__ == '__main__':
    unittest.main()

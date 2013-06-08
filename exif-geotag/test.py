# -*- coding: utf-8 -*-
"""
   test.py
    ~~~~~~~~~~~~~~

    EXIFReader 클래스를 테스트해보기 위한 실행 파일.

    :copyright: (c) 2013 by liks79 [http://www.github.com/liks79]
    :license: MIT LICENSE 2.0, see license for more details.
"""

import exif_reader 

reader = exif_reader.EXIFReader('photos/2012-07-12 12.12.12.jpg')

reader.get_all_exif_data('photos/2012-07-12 12.12.12.jpg')





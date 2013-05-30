#!/usr/bin/python
# -*- coding:utf-8 -*-

import glob;

import EXIF;

#####################


# exif 정보를 읽어올 사진 파일목록을 가져온다.
photos = [];
photos = glob.glob('./photos/*.jpg');

# 파일목록 출
print photos





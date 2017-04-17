#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')


def any_chinese(s):
    return any(u'\u4e00' <= c <= u'\u9fff' for c in s.decode('utf-8'))


def register():
    hooks = ['PreComment']
    print json.dumps(hooks)


def PreComment(content):
    return 0 if any_chinese(content) else 1

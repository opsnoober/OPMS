#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""
import sys #utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.common import auth,index,error

url = [
    (r'/login',auth.LoginHandler),
    (r'/index',index.IndexHandler),
    (r'/logout',auth.LogoutHandler),
    (r'.*',error.PageNotFoundHandler)
]

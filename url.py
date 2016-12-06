#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""
import sys #utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.common import auth,error
from handlers.opms import index
from handlers.opms.daily import daily

url = [
    (r'/',index.IndexHandler),
    (r'/login',auth.LoginHandler),
    (r'/index',index.IndexHandler),
    (r'/logout',auth.LogoutHandler),
  #  (r'.*',error.PageNotFoundHandler),

    (r'/daily/manage_daily',daily.DailyHandler),
    (r'/daily/create_daily',daily.CreateDailyHandler),
    (r'/daily/edit_daily',daily.EditDailyHandler),
]

#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""
import sys #utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")
from handlers import base
from handlers import auth
from handlers.dailyreport import dailyreport
from handlers.api import dailyreportapi
from handlers.api import authapi

urls = [
    (r'/login',auth.LoginHandler),
    (r'/logout',auth.LogoutHandler),
    (r'/index',base.IndexHandler),
    (r'/about',dailyreport.AboutHandler),
    (r'/dailyreport/list',dailyreport.ListDailyReportHandler),
    (r'/dailyreport/add',dailyreport.AddDailyReportHandler),
    (r'/api/dailyreport/list',dailyreportapi.ListApiHandler),
    (r'/api/auth/checklogin',authapi.CheckLoginApiHandler),
]


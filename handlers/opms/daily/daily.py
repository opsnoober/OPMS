#coding:utf-8
import tornado.web
import sys,os
sys.path.append(os.path.dirname((os.path.dirname(os.path.dirname(__file__)))))
from common.base import BaseHandler
from methods.db import DB


class DailyHandler(BaseHandler):

     @tornado.web.authenticated

     def get(self):
        username = self.get_secure_cookie("username")
        sql = 'select * from daily where userid = (select id from user where username="%s")' % username
        rows = DB.query(sql)
        self.render('opms/daily/manage_daily.html',username=username,rows=rows)


class CreateDailyHandler(BaseHandler):

     @tornado.web.authenticated

     def get(self):
        username = self.get_secure_cookie("username")
        self.render('opms/daily/create_daily.html',username=username)

     def post(self):
        username = self.get_secure_cookie("username")
        self.write('hello')


class EditDailyHandler(BaseHandler):

     @tornado.web.authenticated

     def get(self):
        username = self.get_secure_cookie("username")
        self.render('opms/daily/edit_daily.html',username=username)

     def post(self):
        username = self.get_secure_cookie("username")
        self.write('hello')

#coding:utf-8
import tornado.web
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.base import BaseHandler

class IndexHandler(BaseHandler):

     @tornado.web.authenticated

     def get(self):
        username = self.get_secure_cookie("username")
        self.render('opms/index.html',username=username)


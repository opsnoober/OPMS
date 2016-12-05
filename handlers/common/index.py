#coding:utf-8
import tornado.web
from base import BaseHandler

class IndexHandler(BaseHandler):

     @tornado.web.authenticated

     def get(self):
        name = self.get_secure_cookie("username")
        self.render('index.html')


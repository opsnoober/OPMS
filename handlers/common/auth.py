#!/usr/bin/env python
# coding=utf-8
from base import BaseHandler
from methods.db import DB
import json

def check(username,password):
    data = DB.query('select * from user where username = "%s" and password = "%s" '%(username,password))
    if data:
        return True
    else:
        return False


class LoginHandler(BaseHandler):

    '登录页面,用来判断用户名和密码和跳转相应页面'

    def get(self):
        self.render('common/login.html')

    def post(self):
        name = self.get_argument('username')
        passwd = self.get_argument('password')
        obj={}
        if check(name,passwd):
            obj['res'] = 1 #验证通过  
            self.set_secure_cookie("username",name)
            self.redirect('/index')
        else:
            return self.write('''<script>
                alert ("用户名或密码错误!")
                window.location.href="/login"
                </script>
            	''')


class LogoutHandler(BaseHandler):

    '退出登录,清除COOKIE'

    def get(self):
        self.clear_cookie("username")
        self.redirect("/login")


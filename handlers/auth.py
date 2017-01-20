#-*-coding:utf8-*-
import tornado.web
from base import BaseHandler

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html", error=None)

#    def post(self):
#        from utils.md5 import getMD5
#        user = self.db.get("SELECT * FROM user WHERE username = %s",self.get_argument("username"))
#        if not user:
#            #self.render("login.html", error="username not found")
#            self.render("login.html")
#            return
#        hash_password = getMD5(self.get_argument('password'))
#        print "hash_password: %s"%hash_password
#        print "user.password: %s"%user.password
#        if hash_password == user.password:
#            self.set_secure_cookie("user", str(user.id))
#            self.redirect(self.get_argument("next", "/index"))
#        else:
#            self.render("login.html", error="incorrect password")
#            #self.render("login.html")

    def post(self):
#        from utils.md5 import getMD5
#        user = self.db.get("SELECT * FROM user WHERE username = %s",self.get_argument("username"))
#        self.set_secure_cookie("user", str(user.id))
        self.redirect(self.get_argument("next", "/index"))
        #self.redirect("/index")

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/login"))


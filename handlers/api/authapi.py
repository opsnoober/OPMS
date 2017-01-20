from handlers.base import BaseHandler
import tornado.web
from utils.CJsonEncoder import CJsonEncoder
import json

class CheckLoginApiHandler(BaseHandler):
    from utils.md5 import getMD5
 #   @tornado.web.authenticated
    def post(self):
        from utils.md5 import getMD5
        code=0
	message=''
        user = self.db.get("SELECT * FROM user WHERE username = %s",self.get_argument("username"))
        if not user:
            code=1
            message="no such user"
        else:
            hash_password = getMD5(self.get_argument('password'))
            print "hash_password: %s"%hash_password
            print "user.password: %s"%user.password
            if hash_password == user.password:
                code=0
                message="success"
		self.set_secure_cookie("user", str(user.id))
            else:
                code=2
                message="password error"
        res={
	    "code":code,
	    "message":message,
	}
        self.write(json.dumps(res))

#!/usr/bin/env python
import os.path
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from url import urls
from conf import setting
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("address", default="0.0.0.0", help="run on the given address", type=str)
define("mysql_host", default="127.0.0.1:3306", help="opms database host")
define("mysql_database", default="opms", help="opms database name")
define("mysql_user", default="root", help="opms database user")
define("mysql_password", default="secneo", help="opms database password")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls
#        settings = dict(
#            title=u"opms",
#            template_path=os.path.join(os.path.dirname(__file__), "templates"),
#            static_path=os.path.join(os.path.dirname(__file__), "static"),
#            #xsrf_cookies=True,
#            cookie_secret="aZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
#            login_url="/login",
#            debug=True,
#        )
	settings = setting
        super(Application, self).__init__(handlers, **settings)
        # Have one global connection to the blog DB across all handlers
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port,options.address)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

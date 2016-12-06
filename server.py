#!/usr/bin/env python
# coding=utf-8
import tornado.ioloop
import tornado.options
import tornado.httpserver
from application import application
from tornado.options import define, options

define("port", default = 8888, help = "run on the given port", type = int)
define("address", default = '0.0.0.0', help = "run on the given host", type = str)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port,options.address)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print "+++++++++++启动成功+++++++++++"
    main()

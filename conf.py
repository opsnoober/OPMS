#-*-coding:utf8-*-
import os
setting = dict(
            title=u"运维日报系统",
            brand_name=u"运维日报系统",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            #xsrf_cookies=True,
            cookie_secret="aZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            login_url="/login",
            debug=True,
        )


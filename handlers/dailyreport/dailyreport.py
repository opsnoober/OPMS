from handlers.base import BaseHandler
import tornado.web

class ListDailyReportHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        #user_id = self.get_secure_cookie('user')
        #user_id = self.current_user
        #username = self.current_user.username
        #self.render('dailyreport/dailyreport.html',user_id=user_id,username=username)
        self.render('dailyreport/dailyreport.html')

class AddDailyReportHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('dailyreport/add_dailyreport.html')

class AboutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('dailyreport/about.html')



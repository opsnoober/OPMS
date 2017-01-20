from handlers.base import BaseHandler
import tornado.web
from utils.CJsonEncoder import CJsonEncoder
import json

class ListApiHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        userid = int(self.current_user.id)
        offset = int(self.get_argument('offset',0))
        limit = int(self.get_argument('limit',10))
        sort = self.get_argument('sort','daily_id')
        order = self.get_argument('order','desc')
#        argument_data = dict(
#            userid = int(self.current_user.id),
#            offset = int(self.get_argument('offset',0)),
#            limit = int(self.get_argument('limit',10)),
#            sort = self.get_argument('sort','daily_id'),
#            order = self.get_argument('order','desc'),
#       )
        #works = self.db.query('select * from daily where userid = %s order by "%s" "%s" limit %s,%s',userid,sort,order,limit,offset)
        works = self.db.query('select * from daily where userid = %s order by "%s" "%s" limit %s,%s',userid,sort,order,offset,limit)
        total = self.db.query('select count(*) as total from daily where userid = %s',userid)[0]['total']
        worklist = []
        for w in works:
            worklist.append(w)
        res = {
		'message': "success",
		'code': 0,
		'total': total,
		'rows': worklist,
	}
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        res_json = json.dumps(res,cls=CJsonEncoder)
        self.write(res_json)
        
        
        

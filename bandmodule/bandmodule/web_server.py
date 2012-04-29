import web
import json
from model import Band

class BandController(object):
    """ Band"""

    catalog = None
    
    def POST(self, id_):
        self.catalog[id_] = Band(*json.loads(web.data()))

    def GET(self, id_):
        return json.dumps(self.catalog[id_])

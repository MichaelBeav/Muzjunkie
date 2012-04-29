import web
import json
from model import Band

urls = (
    '/band/(.*)', 'BandController'        
)

app = web.application(urls, globals())

class BandController(object):

    catalog = None
    
    def POST(self, id_):
        self.catalog[id_] = Band(*json.loads(web.data()))

    def GET(self, id_):
        return json.dumps(self.catalog[id_])

if __name__ == '__main__':
    app.run()

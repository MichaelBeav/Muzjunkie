import web
import json
from model import Band

urls = (
    '/band/(.*)', 'BandController'        
)

app = web.application(urls, globals())

class BandController(object):

    catalog = dict()
    
    def POST(self, id_):
        self.catalog[id_] = Band(*json.loads(web.data()))
        return ''

    def GET(self, id_):
        try:
            return json.dumps(self.catalog[id_])
        except KeyError:
            return web.notfound('message')

if __name__ == '__main__':
    app.run()

import web
import simplejson as json
from transform import band_to_dict, dict_to_band

urls = (
    '/band/(.*)', 'BandController'        
)

app = web.application(urls, globals())

class BandController(object):

    catalog = dict()
    
    def POST(self, id_):
        band = json.loads(web.data(), object_hook=dict_to_band)
        self.catalog[id_] = band
        web.header('Content-Type', 'text/plain')
        return 'OK'

    def GET(self, id_):
        web.header('Content-Type', 'application/json')
        try:
            band = self.catalog[id_]
            return json.dumps(band, default=band_to_dict)
        except KeyError:
            return web.notfound('Band {} not found'.format(id_))

if __name__ == '__main__':
    app.run()

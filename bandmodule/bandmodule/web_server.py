import web

import transform
from storage import BandCatalog

urls = (
    '/band/(.*)', 'BandController'        
)

app = web.application(urls, globals())

class BandController(object):

    catalog = BandCatalog() # dict()
    
    def POST(self, id_):
        """
        Parse json in request body as band object and
        store it in the catalog.
        """
        band = transform.json_to_band(web.data())
        self.catalog[id_] = band
        web.header('Content-Type', 'text/plain')
        return 'OK'

    def GET(self, id_):
        """
        Return band, represented as json, from catalog.
        """
        web.header('Content-Type', 'application/json')
        try:
            band = self.catalog[id_]
            return transform.band_to_json(band)
        except KeyError:
            return web.notfound('Band {} not found'.format(id_))

if __name__ == '__main__':
    app.run()

from webtest import TestApp
from nose.tools import assert_in, assert_equals

from bandmodule import transform
from bandmodule import web_server
from bandmodule.model import Band
from bandmodule.model import create_band


def create_some_band():
    return Band(name='some name')

class TestBandController(object):

    def setup(self):
        self.band_catalog = dict()
        web_server.BandController.catalog = self.band_catalog
        self.app = TestApp(web_server.app.wsgifunc(*[]))

    def fill_catalog_with(self, key, band):
        self.band_catalog[key] = band

    def on_post_saves_band_in_catalog_test(self):
        band = create_band(name='BandName')
        self.app.post('/band/1', transform.band_to_json(band))
        assert_in('1', self.band_catalog)
        assert_equals(band, self.band_catalog['1'])

    def on_get_returns_band_from_catalog_test(self):
        band = create_band(name='BandName')
        self.fill_catalog_with('1', band)
        response = self.app.get('/band/1')
        res = transform.json_to_band(response.body)
        assert_equals(res, band)

    def on_get_status_is_not_found_if_band_not_found_test(self):
       self.app.get('/band/non-existing-key', status=404)

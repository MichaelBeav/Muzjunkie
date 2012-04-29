import json
from bandmodule import web_server
from bandmodule.model import Band

from webtest import TestApp
from nose.tools import assert_in, assert_equals


def create_some_band():
    return Band(id='1')

def create_band_with(**kwargs):
    return Band(**kwargs)

class TestBandController(object):

    def setup(self):
        self.band_catalog = dict()
        web_server.BandController.catalog = self.band_catalog
        self.app = TestApp(web_server.app.wsgifunc(*[]))

    def fill_catalog_with(self, band):
        self.band_catalog[band.id] = band

    def on_post_saves_band_in_catalog_test(self):
        band = create_band_with(id='1')
        self.app.post_json('/band/1', band)
        assert_in(band.id, self.band_catalog)
        assert_equals(band, self.band_catalog[band.id])

    def on_get_returns_band_from_catalog_test(self):
        band = create_band_with(id='1')
        self.fill_catalog_with(band)
        response = self.app.get('/band/1')
        res = json.loads(response.body)
        assert_equals(Band(*res), band)



#import json
from bandmodule import web_server
from bandmodule.model import Band

from webtest import TestApp
from nose.tools import assert_in, assert_equals

class TestBandController(object):

    def setup(self):
        self.band_catalog = dict()
        web_server.BandController.catalog = self.band_catalog
        self.app = TestApp(web_server.app.wsgifunc(*[]))

    def on_post_saves_band_in_catalog_test(self):
        band = Band(id='1')
        self.app.post_json('/band/1', band)
        assert_in(band.id, self.band_catalog)
        assert_equals(band, self.band_catalog[band.id])


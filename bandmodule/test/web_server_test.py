import json
from pyvows import Vows, expect
from bandmodule import web_server
from bandmodule.model import Band

@Vows.create_assertions
def to_contain_entry(topic, entry):
    """
    Test if given dict-like object contains
    given key-value pair.
    """
    key, value = entry
    return key in topic and topic[key] == value

@Vows.batch
class BandHandler(Vows.Context):

    def topic(self):
        band_catalog = dict()
        web_server.BandController.catalog = band_catalog
        return band_catalog
    
    class OnPostBand(Vows.Context):

        def topic(self, band_catalog):
            band = Band(id='1')
            def mock_data():
                return json.dumps(band)
            web_server.web.data = mock_data
            band_controller = web_server.BandController()
            band_controller.POST(band.id)
            return band, band_catalog

        def saves_band_in_band_catalog(self, topic):
            band, band_catalog = topic
            expect(band_catalog).to_contain_entry((band.id, band))

    class OnGetBand(Vows.Context):

        def topic(self, band_catalog):
            band_id = 'band_id'
            band = Band(band_id)
            band_catalog[band_id] = band
            return band, web_server.BandController().GET(band_id)

        def returns_band_as_json(self, topic):
            band, get_result = topic
            result_band = Band(*json.loads(get_result))
            expect(result_band).to_equal(band)

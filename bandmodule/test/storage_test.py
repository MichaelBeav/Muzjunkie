import pickle
from nose.tools import assert_equals
from mock import patch

from bandmodule.model import create_band
from bandmodule.storage import BandCatalog


class TestBandCatalog(object):

    def setup(self):
        # patcher mocks all methods of the class
        self.patcher = patch('redis.StrictRedis')
        self.redis_mock = self.patcher.start().return_value

    def teardown(self):
        self.patcher.stop()

    @patch('pickle.loads')
    def getitem_calls_redis_get_test(self, loads_mock):
        BandCatalog()['BandKey']
        self.redis_mock.get.assert_called_once_with('BandKey')

    def getitem_deserializes_result_test(self):
        band = create_band(name='Metalizer')
        self.redis_mock.get.return_value = pickle.dumps(band)
        assert_equals(band, BandCatalog()['AnyKey'])

    def setitem_calls_redis_set_test(self):
        BandCatalog()['BandKey'] = 'anything'
        assert_equals(1, self.redis_mock.set.call_count)

    def setitem_serializes_value_test(self):
        band = create_band(name='BandName')
        BandCatalog()['BandKey'] = band
        self.redis_mock.set.assert_called_once_with('BandKey',
                                            pickle.dumps(band))

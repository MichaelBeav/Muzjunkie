import simplejson as json
from nose.tools import assert_in, assert_equals

from bandmodule.model import create_band
from bandmodule.transform import band_to_dict, dict_to_band

def some_band():
    return create_band(name='SomeBand')

def band_to_json_test():
    result_str = json.dumps(some_band(), default=band_to_dict)
    result_dict = json.loads(result_str)
    assert_in('name', result_dict)
    assert_equals('SomeBand', result_dict['name'])

def json_to_band_test():
    band = some_band()
    js = json.dumps({'name': 'SomeBand'})
    result_band = json.loads(js, object_hook=dict_to_band)
    assert_equals(band, result_band)

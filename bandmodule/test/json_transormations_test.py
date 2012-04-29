import simplejson as json
from nose.tools import assert_in, assert_equals

from bandmodule.model import Band
from bandmodule.transform import band_to_dict, dict_to_band

def some_band():
    return Band(id='band_id')

def band_to_json_test():
    result_str = json.dumps(some_band(), default=band_to_dict)
    result_dict = json.loads(result_str)
    assert_in('id', result_dict)
    assert_equals('band_id', result_dict['id'])

def json_to_band_test():
    band = Band(id='some_id')
    js = json.dumps({'id': 'some_id'})
    result_band = json.loads(js, object_hook=dict_to_band)
    assert_equals(band, result_band)

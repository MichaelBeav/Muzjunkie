import simplejson as json
from nose.tools import assert_in, assert_equals

from bandmodule.model import create_band
from bandmodule.transform import band_to_json, json_to_band

def band_to_json_test():
    band = create_band(name='SomeBand')
    result_str = band_to_json(band)
    result_dict = json.loads(result_str)
    assert_in('name', result_dict)
    assert_equals(band.name, result_dict['name'])

def json_to_band_test():
    json = """{
            "name": "Fasten Pelvis",
            "genres": [ "salsa", "vahtang" ],
            "avatar": "http://goo.gl/CjLGT"
        }"""
    band = json_to_band(json)
    assert_equals(band.name, "Fasten Pelvis")
    assert_in("salsa", band.genres)
    assert_in("vahtang", band.genres)
    assert_equals(band.avatar, "http://goo.gl/CjLGT")

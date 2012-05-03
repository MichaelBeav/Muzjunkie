import simplejson as json

from model import Band
from model import create_band

__all__ = ['band_to_json', 'json_to_band']

def band_to_dict(band):
    if isinstance(band, Band):
        return band._asdict()
    raise TypeError("{} is not a Band object".format(band))

def dict_to_band(dic):
    return create_band(**dic)

def band_to_json(band):
    return json.dumps(band, default=band_to_dict)

def json_to_band(js):
    return json.loads(js, object_hook=dict_to_band)

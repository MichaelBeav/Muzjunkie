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

def lastfm_artist_to_band(artist):
    band_dict = {}
    artist = artist['artist']
    band_dict['name'] = artist['name']
    band_dict['primary_genre'] = artist['tags']['tag'][0]['name']
    band_dict['genres'] = map(
            lambda tag: tag['name'],
            artist['tags']['tag'][1:4])

    band_dict['bio'] = artist['bio']['summary']
    return create_band(**band_dict)


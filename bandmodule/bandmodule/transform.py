from model import Band
from model import create_band

def band_to_dict(band):
    if isinstance(band, Band):
        return band._asdict()
    raise TypeError("{} is not a Band object".format(band))

def dict_to_band(dic):
    return create_band(**dic)


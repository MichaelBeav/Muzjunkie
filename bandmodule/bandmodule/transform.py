from model import Band

def band_to_dict(band):
    if isinstance(band, Band):
        return {'id': band.id}
    raise TypeError("{} is not a Band object".format(band))

def dict_to_band(dic):
    return Band(**dic)


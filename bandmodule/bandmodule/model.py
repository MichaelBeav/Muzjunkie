from collections import namedtuple
from copy import deepcopy

_band_fields = {
        'name': '',
        'bio': '',
        'primary_genre': '',
        'genres': [],
        'status': '',
        'country': '',
        'region': '',
        'city': '',
        'members': '',
        'avatar': '',
        'similar_artists': '',
        'raider': '',
        'rid' : '', }

Band = namedtuple('Band', _band_fields.keys())

def create_band(**kwargs):
    """ Factory method for creating
    partially field `Band`. Fields, that are not
    given in kwargs, are set do default
    """

    fields = deepcopy(_band_fields)
    needed_arg_names = filter(lambda name: name in _band_fields,
                              kwargs)
    for name in needed_arg_names:
        fields[name] = kwargs[name]
    return Band(**fields)

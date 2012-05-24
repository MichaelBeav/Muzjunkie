import api
from bandmodule import transform
from bandmodule.storage import RedisBandCatalog


def top_artists_for_user(username, band_collection):
    top = api.get_top_artists_for_user(username)
    top_info = map(
            lambda t: api.get_artist_info(t['name']),
            top['topartists']['artist'][:5])
    print(top_info[0].keys())
    band_list = map(
            transform.lastfm_artist_to_band,
            top_info)

    for band in band_list:
        band_collection[band.name] = band
    return band_list

if __name__ == '__main__':
    d = RedisBandCatalog()
    print(top_artists_for_user('filipovskii_off', d))

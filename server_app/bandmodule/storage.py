import redis
import pickle
import os, urlparse


class RedisBandCatalog(object):
    """
    Redis-based implementation of band catalog.
    Usage:
        band_catalog['key'] = value   # stores value under given key
        value = band_catalog['key']   # retrieves value
    """

    def __init__(self):
        if os.environ.has_key('REDISTOGO_URL'):
            urlparse.uses_netloc.append('redis')
            url = urlparse.urlparse(os.environ['REDISTOGO_URL'])
            self._redis_instance = redis.Redis(host=url.hostname,
                                               port=url.port, db=0,
                                               password=url.password)
        else:
            self._redis_instance = redis.StrictRedis(host='localhost',
                                                     port=6379, db=0)

    def __getitem__(self, item):
        band_serialized = self._redis_instance.get(item)
        if band_serialized:
            return pickle.loads(band_serialized)
        raise KeyError('Band with key "{}" not found'.format(item))

    def __setitem__(self, item, value):
        return self._redis_instance.set(item, pickle.dumps(value))

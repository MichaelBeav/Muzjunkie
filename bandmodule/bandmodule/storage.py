import redis

class BandCatalog(object):

    def __init__(self):
        self._redis_instance = redis.StrictRedis(host='localhost',
                                                 port=6379, db=0)

    def __getitem__(self, item):
        return self._redis_instance.get(item)

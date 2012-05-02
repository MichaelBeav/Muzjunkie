import redis
import pickle

class BandCatalog(object):

    def __init__(self):
        self._redis_instance = redis.StrictRedis(host='localhost',
                                                 port=6379, db=0)

    def __getitem__(self, item):
        return pickle.loads(self._redis_instance.get(item))

    def __setitem__(self, item, value):
        return self._redis_instance.set(item, pickle.dumps(value))

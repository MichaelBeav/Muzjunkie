import redis
from mock import patch
from bandmodule.storage import BandCatalog

def getitem_calls_redis_get_test():
    with patch('redis.StrictRedis') as StrictRedisMock:
        redis_mock = StrictRedisMock.return_value
        BandCatalog()['BandKey']
        redis_mock.get.assert_called_once_with('BandKey')


# -*- coding: utf-8 -*-

import redis

class Database(object):

    def __init__(self, host='localhost', port=6379, db=0):
	self.db = redis.Redis(host=host, port=port, db=db)
    
    #INTERFACE:
    
    #Get object by key
    def get(self, key):
	return self.db.get(key)
    
    #Store Data under the Key
    def set(self, key, data) :
	if self.db.set(key, data):
	    return self.db.get(key)
	else:
	    return None
    
    #Delete the object stored by the Key from DB:
    def delete(self, key):
	return self.db.delete(key)
    
    #Get Set object from Redis
    def get_set(self, key):
	return self.db.smembers(key)

    #Store Set object inside Redis Set data type object:
    def store_set(self, key, data):
	if type(data) == type([]):
	    return self.db.sadd(key, *data)
	else:
	    return False

    #Get hash object from Redis
    def get_hash(self, key):
	return self.db.hgetall(key)
    
    #Store Hash object inside Redis Hash data type object:
    def set_hash(self, key, data):
	if type(data) == type({}):
	    return self.db.hmset(key, data)
	else:
	    return False

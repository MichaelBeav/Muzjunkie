# -*- coding: utf-8 -*-

class KVStorage(object):
    
    def __init__(self, engine, **kwargs):
	self.db = False
	self.engine = engine
	
	#Format - engine: python_module_name
	self.supported_engines = {
	    'redis': 'redis_wrapper'
	}
	
	if self.supported_engines.has_key(self.engine):
	    self._init_db(kwargs)
	else:
	    raise Exception('Unsoported Database Engine: %s' % (self.engine))
    
    
    def _init_db(self, kwargs):
	module = __import__(self.supported_engines[self.engine])
	self.db = module.Database(**kwargs)

    #INTERFACE FOR IMPLEMENTATION IN WRAPPERS:
    
    #GET OBJECT BY KEY:
    def get(self, key):
	return self.db.get(key)
    
    #Save KEY
    def set(self, key, data):
	return self.db.set(key, data)
    
    #Delete key:
    def delete(self, key):
	return self.db.delete(key)
    
    #Get hash. Some DB supports Hashes nativaly (i.e. - Redis). Other wrappers will need to implement this behaviour
    def get_hash(self, key):
	return self.db.get_hash(key)

    #Store Hash. Some DB supports Hashes nativaly (i.e. - Redis). Other wrappers will need to implement this behaviour
    def set_hash(self, key, data):
	return self.db.set_hash(key, data)

    #Get set. Some DB supports sets nativaly (i.e. - Redis). Other wrappers will need to implement this behaviour
    def get_set(self, key):
	return self.db.get_set(key)
    
    #Store set. Some DB supports sets nativaly (i.e. - Redis). Other wrappers will need to implement this behaviour
    def store_set(self, key, data):
	return self.db.store_set(key, data)

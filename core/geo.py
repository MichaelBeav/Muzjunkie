# -*- coding: utf-8 -*-
from RESTful import RESTful

class MJCountry(RESTful):
    
    def __init__(self, db, base_url=""):
	#Init RESTful superclass
	super(MJCountry, self).__init__(base_url = base_url)    
        self.db = db
        
        #References to DB Keys:
        self.main_key_prefix = "/country/"
        self.resource_prefix = "profile:"
	
	#Resource Object structure. Keep the fields in model for consistence:
	self.resource_attributes = {
	    'name': '',
	    'alpha2_name': '',
	    'official_name': '',
	    'regions': [],
	    'rid': '',
	}
	
    ##RESTful implementation:
    @classmethod
    def get_featured(cls):
	pass
    
    #Export db keys for scripting
    @classmethod
    def get_db_keys_layout(cls):
	db_keys = {
	    'main_key_prefix': cls.main_key_prefix,
	    'resource_prefix': cls.resource_prefix,
	    'resource_attributes': cls.resource_attributes
	}
	
	return db_keys
        
    def get_resource(self, name):
	resource_key = "%s%s%s" % (self.main_key_prefix, self.resource_prefix, name)
	main_profile = self.db.get_hash(resource_key)
	
	#Extend result with resource id:
	main_profile['rid'] = "%s%s%s" % (self.base_url, self.main_key_prefix, name)
	
	#Get regions for Country:
	regions = MJCountryRegions(self.db, base_url=self.base_url)
	main_profile['regions'] = regions.get_resource(name)
	
	#Apply self.resource_attributes dict to the result to keep consisten output even if the fields are absent uneder object returned from DB
	resource =  dict(self.resource_attributes.items() + main_profile.items())
	return resource
    
    def update_object(self, name, data):
	pass
    
    def delete_object(self, name):
	
	return {'result': 'ok'}
    
    def put_object(self, name, data):
	resource_key = "%s%s%s" % (self.main_key_prefix, self.resource_prefix, name)
	
	if (self.db.set_hash(resource_key, data)):
	    return self.get_resource(name)
	else:
	    return {}

class MJCountryRegions(RESTful):
    
    def __init__(self, db, base_url=""):
	#Init RESTful superclass
	super(MJCountryRegions, self).__init__(base_url = base_url)    
        self.db = db
        
        #References to DB Keys:
        self.main_key_prefix = "/country/"
        self.resource_prefix = "regions:"
	
	#!!Fixme: this should come from MJCountryRegion object classmethod when will be created
	self.sigleton_object_main_key = "/country_region/"	
	
    ##RESTful implementation:
    @classmethod
    def get_featured(cls):
	return {}
    
    def get_resource(self, name):
	ret = []
	resource =  self.db.get_set("%s%s%s" % (self.main_key_prefix, self.resource_prefix, name))
	
	#We have a set of objects. Need to return list of objects with resource ids to follow the RESTful rules:
	if len(resource):
	    for res in resource:
		ret.append({'name': res, 'rid': "%s%s%s" % (self.base_url, self.sigleton_object_main_key, res)})
	
	return ret
    
    def update_object(self, name, data):
	pass
    
    def delete_object(self, name):
	return {'result': 'ok'}
    
    def put_object(self, name, data):
	resource_key = "%s%s%s" % (self.main_key_prefix, self.resource_prefix, name)
	if self.db.store_set(resource_key, data):
	    return self.get_resource(name)
	else:
	    return {}

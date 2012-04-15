from RESTful import RESTful

class MJBand(RESTful):
    
    def __init__(self, db, base_url=""):
	#Init RESTful superclass
	super(MJBand, self).__init__(base_url = base_url)    
        self.db = db
        
        #References to DB Keys:
        self.main_key_prefix = "/band/"
        self.resource_prefix = "profile:"
	
	#Resource Object structure. Keep the fields in model for consistence:
	self.resource_attributes = {
	    'band_name': '',
	    'bio': '',
	    'primary_genre': '',
	    'genres': [], 
	    'status': '',
	    'country': '',
	    'region': '',
	    'city': '',
	    'members': [],
	    'avatar': '',
	    'similar_artists': [],
	    'raider': '',
	    'rid': ''
	}
	
    ##RESTful implementation:
    @classmethod
    def get_featured(cls):
	pass
    
    def get_resource(self, name):
    
	#Get main band profile:
	main_profile = self.db.get_hash("%s%s%s" % (self.main_key_prefix, self.resource_prefix, name))
	if not len(main_profile):
	    return self.not_exists_return
	
	#Extend result with resource id:
	main_profile['rid'] = "%s%s%s" % (self.base_url, self.main_key_prefix, name)
	
	#Get Secondary genres:
	sg = MJSecondaryGenres(self.db, base_url=self.base_url)
	main_profile['genres'] = sg.get_resource(name)
	
	#Apply self.resource_attributes dict to the result to keep consisten output even if the fields are absent uneder object returned from DB
	resource =  dict(self.resource_attributes.items() + main_profile.items())
	return resource
    
    def update_object(self, name, data):
	pass
    
    def delete_object(self, name):
	
	return {'result': 'ok'}
    
    def put_object(self, name, data):
	pass


class MJSecondaryGenres(RESTful):
    
    def __init__(self, db, base_url=""):
	#Init RESTful superclass
	super(MJSecondaryGenres, self).__init__(base_url=base_url)
        self.db = db
        
        #References to DB Keys:
        self.main_key_prefix = "/band/"
        self.resource_prefix = "secondary_genres:"
	
	#!!Fixme: this should come from MJSecondaryGenre object classmethod when will be created
	self.sigleton_object_main_key = "/secondary_genre/"

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
	pass

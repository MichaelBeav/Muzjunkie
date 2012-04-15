import re
import json

VALID_KEY = re.compile('[a-zA-Z0-9_-]{1,255}')
def is_valid_key(key):
    """Checks to see if the parameter follows the allow pattern of
    keys.
    """
    if VALID_KEY.match(key) is not None:
	return True
    
    return False
                            
def validate_key(fn):
    """Decorator for HTTP methods that validates if resource
    name is a valid database key.
    """
    def new(*args):
	if not is_valid_key(args[1]):
	    web.badrequest()
	return fn(*args)
    
    return new

class RESTful(object):
    """Abstract class to handle high-level HTTP/RESTful primitives
    """
    
    def __init__(self, base_url=""):
	self.base_url = base_url
	self.not_exists_return = {}
    
    @validate_key
    def GET(self, name):
	if len(name) <= 0:
	    return josn.dumps(self.get_featured())
	else:
	    return json.dumps(self.get_resource(name))
    
    @validate_key
    def POST(self, name):
	data = web.data()
        updated_object = self.update_object(str(name), data)
	return json.dumps(updated_object)
    
    @validate_key
    def DELETE(self, name):
	self.delete_object(str(name))
    
    @validate_key
    def PUT(self, name):
	data = web.data()
	new_object = self.put_object(name, data)	
	return json.dupms(new_object)



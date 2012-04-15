#!/usr/bin/python

import web

#Local Classes:
from band import MJBand, MJSecondaryGenres
from kv_storage import KVStorage

urls = (
    '/secondary_genres/(.*)', 'SecondaryGenres',
    '/band/(.*)', 'Band',
    '/(.*)', 'Band'
)

app = web.application(urls, globals())

db = KVStorage('redis', host="localhost", port=6379, db=0)
base_url = "http://localhost:8080"


#MAIN BAND PROFILE RESTFUL WRAPPER
class Band:    
    #RESTful GET method:
    def GET(self, band_name=None):
	if band_name:
	    band = MJBand(db, base_url=base_url)
	    
	    web.header("Content-Type", "application/json")
	    return(band.GET(band_name))
	    
	else:
	    return "Featured"


#RESTFUL WRAPPER TO CONTROL SECONDARY GENRES FOR THE BAND
class SecondaryGenres:
    #RESTful GET method:
    def GET(self, band_name=None):
	if band_name:
	    sg = MJSecondaryGenres(db, base_url=base_url)
	    
	    web.header("Content-Type", "application/json")
	    return(sg.GET(band_name))
	else:
	    return "Featured"    

if __name__ == "__main__": app.run()

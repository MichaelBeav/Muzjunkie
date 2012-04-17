#!/usr/bin/python
# -*- coding: utf-8 -*-

import lastfm
import pycountry
import sys

sys.path.insert(0, '../')

#local imports:
from redis_wrapper import Database
from mj_utils import slugify
from geo import MJCountry, MJCountryRegions

def main():
    db = Database(host="localhost", port=6379, db=0) 
    lastfm_api_key = '859c141d1935469873ff2df3300047c3'
    lastfm_api = lastfm.Api(lastfm_api_key)
    
    init_geo(db)
    #Number of Bands to be created
    bands = 10


def init_bands(lastfm_api, db):
    artist = lastfm_api.get_artist('A Day To Remember')
    similar_artists = artist.similar
    for a in similar_artists[:bands]:
	band_name = a.name
	band_bio = a.bio
	tags = a.top_tags[:3]
	primary_genre = tags[0].name
	secondary_genres = [x.name for x in tags[1:3]]
	
	status = ''
	country = ''
	
	print "%s %s %s %s" % (band_name, primary_genre, secondary_genres, band_bio.summary)

def init_geo(db):

    countries = pycountry.countries
    for country in countries:
	#Get regions for the Country: 
	try:
	    regions = [slugify(x.name) for x in pycountry.subdivisions.get(country_code=country.alpha2)]
	except:
	    regions = []
	
	country_key = slugify(country.name)

	if len(regions):
	    regions_obj = MJCountryRegions(db, base_url = "http://localhost:8080")
	    #Calling put_object method directly instead of doing that via the RESTful class:
	    regions_obj.put_object(country_key, regions)
	    print "Saving Geo Regions for: %s" % (country_key)
	
	try:
	    official_name = country.official_name
	except:
	    official_name = country.name

	country_hash = {
	    'name': country.name,
	    'alpha2_name': country.alpha2,
	    'official_name': official_name,
	}
	
	country_obj = MJCountry(db, base_url = "http://localhost:8080")
	#Saving info about the Country by calling the put_object method of the MJCountry directly without calling the RESTful.PUT()
	country_obj.put_object(country_key, country_hash)
	print "Saving Country Data for: %s" % (country_key)

if __name__ == "__main__": 
    main() 
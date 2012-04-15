#!/usr/bin/python
import redis
import lastfm

def main():
    db = redis.Redis(host="localhost", port=6379, db=0) 
    lastfm_api_key = '859c141d1935469873ff2df3300047c3'
    lastfm_api = lastfm.Api(lastfm_api_key)
   
    #Number of Bands to be created
    bands = 10
   
    artist = lastfm_api.get_artist('A Day To Remember')
    similar_artists = artist.similar
    for a in similar_artists[:bands]:
	band_name = a.name
	band_bio = a.bio
	tags = a.top_tags[:3]
	primary_genre = tags[0].name
	secondary_genres = [x.name for x in tags[1:3]]
	
	print "%s %s %s %s" % (band_name, primary_genre, secondary_genres, band_bio.summary)

if __name__ == "__main__": 
    main() 
import hashlib
import urllib2
import simplejson as json
import webbrowser
from os import environ

API_KEY = '105808eea1044f14d02f77291496a023'
ROOT_URL = 'http://ws.audioscrobbler.com/2.0/'
SECRET = 'c88dd553de237cdabffb06d4d82e9207'

def create_session():
    try:
        with open(environ['HOME'] + '/.lastfmsession', 'r') as session_file:

            # session is already opened
            username = session_file.readline()[:-1]
            key_str = session_file.readline()[:-1]
            if username and key_str:
                return username, key_str
    except IOError: # file doesn't exist
        pass

    with open(environ['HOME'] + '/.lastfmsession', 'w') as session_file:

        # session is not opened -> open
        if 'htt_proxy' in environ:
            proxy = urllib2.ProxyHandler({'http': environ['http_proxy']})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)

        token_url = _make_request_url(method='auth.gettoken', api_key=API_KEY)
        token_response = urllib2.urlopen(token_url)
        token = json.loads(token_response.read())['token']

        webbrowser.open('http://www.last.fm/api/auth/?api_key={}&token={}'
                        .format(API_KEY, token))
        print('Authorize request in your browser, then press Enter')
        raw_input()

        session_req_url = _make_signed_request_url(
                                                method='auth.getsession',
                                                token=token,
                                                api_key=API_KEY)
        
        session_response = urllib2.urlopen(session_req_url)

        response_dict = json.loads(session_response.read())

        key = response_dict['session']['key']
        name = response_dict['session']['name']
        session_file.write(name + '\n')
        session_file.write(key + '\n')
        return name, key

def _make_request_url(**kwargs):
    url = ROOT_URL[:] + '?'
    for key, val in kwargs.items():
        url += '{}={}&'.format(key, val)
    url += 'format=json'
    return url

    
def _make_signed_request_url(**kwargs):
    md5 = hashlib.md5()
    for key in sorted(kwargs):
        md5.update('{}{}'.format(key, kwargs[key]))
    md5.update(SECRET)
    kwargs['api_sig'] = md5.hexdigest()
    return _make_request_url(**kwargs)
    

if __name__ == '__main__':
    username, session_key = create_session()
    top_artists_str = urllib2.urlopen(_make_request_url(
        method='user.getTopArtists',
        user=username,
        api_key=API_KEY)).read()
    top_artists_dict = json.loads(top_artists_str)
    print(top_artists_dict)

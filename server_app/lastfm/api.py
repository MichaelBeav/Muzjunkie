import hashlib
import urllib2
import simplejson as json
import webbrowser
from os import environ

API_KEY = '105808eea1044f14d02f77291496a023'
ROOT_URL = 'http://ws.audioscrobbler.com/2.0/'
SECRET = 'c88dd553de237cdabffb06d4d82e9207'

def create_session():
    if 'htt_proxy' in environ:
        proxy = urllib2.ProxyHandler({'http': environ['http_proxy']})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
    token_response = urllib2.urlopen(
                   '{}?method=auth.gettoken&api_key={}&format=json'
                   .format(ROOT_URL, API_KEY))
    token = json.loads(token_response.read())['token']

    webbrowser.open('http://www.last.fm/api/auth/?api_key={}&token={}'
                    .format(API_KEY, token))
    print('authorize request in your browser, then press any key')
    raw_input()

    session_req_url = _make_signed_request_url(
                                            method='auth.getsession',
                                            token=token,
                                            api_key=API_KEY)
    
    session_req_url += '&format=json' # format should not be in api_sig
    print(session_req_url)
    session_response = urllib2.urlopen(session_req_url)

    print(session_response.read())
    raw_input()
    
def _make_signed_request_url(**kwargs):
    md5 = hashlib.md5()
    url = ROOT_URL[:] + '?'
    for key in sorted(kwargs):
        url += '{}={}&'.format(key, kwargs[key])
        md5.update('{}{}'.format(key, kwargs[key]))
    md5.update(SECRET)
    url += 'api_sig={}'.format(md5.hexdigest())
    return url
    

if __name__ == '__main__':
    create_session()

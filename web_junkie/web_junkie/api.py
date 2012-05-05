import foauth2
import web
from urllib2 import HTTPError

client_ID = '473166131441.apps.googleusercontent.com'
client_SECRET = 'Vtfzj65FiBUikU3WD6lH8Qkh'
SCOPE = 'https://www.google.com/m8/feeds/'
REDIRECT_URI = 'http://localhost:8080/callback' # url to your server here
API_URI = 'https://www.google.com/m8/feeds/contacts/default/full'

render = web.template.render('templates/')

urls = (
    '/',     'Index',
    '/auth-url', 'Auth',
    '/callback', 'Login'
)
client = foauth2.GooglAPI(client_ID, client_SECRET)

app = web.application(urls, globals())

class Index(object):

    def GET(self):
        return render.index()

class Auth(object):
    
    def GET(self):
        return '<a href={}>Authorize</a>'.format(authorize_url())

class Login(object):

    def GET(self):
        code = web.input(name='code').code
        try:
            get_token(code)
            return client.request(API_URI, None, 
                    {'Content-Type': 'application/json'},
                    'GET')
        except HTTPError, e:
            return e.read()


def authorize_url():
    return client.authorization_url(
            redirect_uri=REDIRECT_URI,
            scope=SCOPE)

def get_token(code):
    return client.redeem_code(
            refresh_uri='https://accounts.google.com/o/oauth2/token',
            redirect_uri=REDIRECT_URI,
            code=code,
            scope=SCOPE)

if __name__ == '__main__':
    app.run()

#import json
from bandmodule import web_server
#from bandmodule.model import Band

from webtest import TestApp
#from nose.tools import *

class TestBandController(object):

    def setup(self):
        self.app = TestApp(web_server.app.wsgifunc(*[]))

    def smth_test(self):
        print(self.app)

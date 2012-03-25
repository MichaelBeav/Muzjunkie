import unittest
from web_junkie import api

class TetsOauth(unittest.TestCase):

    def test_simple_auth_generation(self):
        """ Tests nothing, actually"""
        resp = api.authorize_url()
        print(resp)

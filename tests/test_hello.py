import unittest
import json
from application import app
from application.common import Map


class HelloTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.name = "world"

    def tearDown(self):
        pass

    def test_hello_response(self):
        rv = self.app.get('/v1.0/hello/%s' % self.name)
        data = Map(json.loads(rv.data))
        assert data.message == "Hello %s" % self.name

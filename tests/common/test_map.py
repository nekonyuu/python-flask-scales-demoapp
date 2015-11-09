import unittest
from application.common import Map


class MapTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_map_content(self):
        src = dict()
        src.update({
            "a": "b"
        })

        src_map = Map(src)
        assert src_map.a == src["a"]

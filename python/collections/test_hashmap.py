from unittest import TestCase

from python.collections.hashmap import HashMap


class TestHashMap(TestCase):
    def test_basic(self):
        pass
        m = HashMap()

        m.put("abc", "123")
        self.assertEqual(m.get("abc"), "123")

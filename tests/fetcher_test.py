from fetcher import Fetch
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        f = Fetch()
        
        self.assertEqual(f.value(), 1)

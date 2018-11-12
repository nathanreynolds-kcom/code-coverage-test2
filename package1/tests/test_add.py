import os.path
import sys
import unittest

sys.path = [os.path.dirname(__file__) + '/../src'] + sys.path

import add

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add.add(5, 20), 25)

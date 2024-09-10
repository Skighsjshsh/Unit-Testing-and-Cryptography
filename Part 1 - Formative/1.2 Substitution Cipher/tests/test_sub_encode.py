from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode
class MyTestCase(TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here



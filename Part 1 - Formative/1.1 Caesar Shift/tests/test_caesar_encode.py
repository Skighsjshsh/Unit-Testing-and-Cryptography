from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode
class MyTestCase(unittest.TestCase):
    def test_caesar_encode_uppercase(self):
        self.assertEqual(caesar_encode(text, n), "MJQQTBTWQI")

    def test_caesar_encode_uppercase(self):
        self.assertEqual(caesar_encode(text, n), "mjqqtbtwqi")



if __name__ == '__main__':
    unittest.main()

from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode

class MyTestCase(TestCase):
        def test_vig_encode_uppercase(self):
            self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", "TEST"), "MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ")

        def test_vig_encode_lowercase(self):
            self.assertEqual(vig_encode("thequickbrownfoxjumpedoverthelazydog", "TEST"), "MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ")

        def test_vig_encode_spaces(self):
            self.assertEqual(vig_encode("THE QUICK BROWN FOX JUMPED OVER THE LAZYDOG", "TEST"), "MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ")

        def test_vig_encode_empty(self):
            self.assertEqual(vig_encode("", "TEST"), "")



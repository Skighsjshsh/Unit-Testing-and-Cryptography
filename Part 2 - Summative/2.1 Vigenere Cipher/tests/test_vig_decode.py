from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode

class MyTestCase(TestCase):
        def test_vig_decode_uppercase(self):
            self.assertEqual(vig_decode("MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ", "TEST"), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")

        def test_vig_decode_lowercase(self):
            self.assertEqual(vig_decode("mlwjnmuduvgpgjgqcyeixhgoxvlaxpssrhgz", "TEST"), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")

        def test_vig_decode_spaces(self):
            self.assertEqual(vig_decode("MLWJNM UDUVGPGJGQ CYEIXHG OXVLAX PSSRHGZ", "TEST"), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")

        def test_vig_decode_empty(self):
            self.assertEqual(vig_decode("", "TEST"), "")



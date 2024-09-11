from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode
class MyTestCase(TestCase):
    def test_sub_decode_uppercase(self):
        self.assertEqual(sub_decode("MXTTHAHOTU", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HELLOWORLD")

    def test_sub_decode_lowercase(self):
        self.assertEqual(sub_decode("mxtthahotu", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HELLOWORLD")

    def test_sub_decode_space(self):
        self.assertEqual(sub_decode("MXTTH AHOTU", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HELLOWORLD")
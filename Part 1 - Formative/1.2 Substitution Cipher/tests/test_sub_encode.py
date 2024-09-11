from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode
class MyTestCase(TestCase):
    def test_sub_enocde_uppercase(self):
        self.assertEqual(sub_encode("HELLOWORLD", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MXTTHAHOTU")

    def test_sub_enocde_lowercase(self):
        self.assertEqual(sub_encode("helloworld", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MXTTHAHOTU")

    def test_sub_enocde_space(self):
        self.assertEqual(sub_encode("HELLO WORLD", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MXTTHAHOTU")
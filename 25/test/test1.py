#!/usr/bin/python3
import unittest
import step1

class TestStep1TestInputLength(unittest.TestCase):
    def runTest(self):
        self.assertEqual("2=-1=0", step1.read_drawing("test/input"))

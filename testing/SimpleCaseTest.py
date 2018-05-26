# -*- coding: utf-8 -*-
import unittest


class TestStringMethods(unittest.TestCase):

    def test_assertTrue(self):
        self.assertEqual(True, True)

    @unittest.skip("Skip failing test")
    def test_shouldFail(self):
        self.assertEqual(True, False)

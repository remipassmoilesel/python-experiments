# -*- coding: utf-8 -*-
import unittest


class SimpleCaseTest(unittest.TestCase):

    def test_assertTrue(self):
        self.assertEqual(True, True)

    def assertFail(self):
        with self.assertRaises(Exception):
            raise Exception()

    @unittest.skip("Skip failing test")
    def test_shouldFail(self):
        self.assertEqual(True, False)

    @unittest.expectedFailure
    def test_expectedFailure(self):
        self.fail("This test can fail, and will be ignored")
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
from script import *

class ScriptTest(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, DoSomething().please())

if __name__ == '__main__':
    unittest.main()
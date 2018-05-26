# -*- coding: utf-8 -*-
import unittest
from unittest.mock import MagicMock
from src import TestObject


class MockTest(unittest.TestCase):

    def test_mockMethod(self):
        testInstance = TestObject()
        testInstance.sayHello = MagicMock(return_value=3)
        self.assertEqual(testInstance.sayHello(), 3)
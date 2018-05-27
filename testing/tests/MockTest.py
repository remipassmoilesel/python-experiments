# -*- coding: utf-8 -*-
import unittest
from unittest.mock import MagicMock, patch
from src import TestObject


class MockTest(unittest.TestCase):

    def test_mockMethod(self):
        testInstance = TestObject()
        testInstance.sayHello = MagicMock(return_value=3)
        self.assertEqual(testInstance.sayHello(), 3)

    @patch('src.TestObject.sayHello', return_value=9)
    def test_mockMethod2(self, sayHello):
        self.assertEqual(sayHello(), 9)

    @patch('src.TestObject.sayHelloTo', return_value=10)
    def test_mockMethod2(self, sayHelloTo):
        self.assertEqual(sayHelloTo("Bob"), 10)
        sayHelloTo.assert_called_with("Bob")
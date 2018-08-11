# -*- coding: utf-8 -*-
import unittest
from unittest.mock import MagicMock, patch

from src.TestObject import TestObject


class MockTest(unittest.TestCase):

    def test_mockMethod(self):
        testInstance = TestObject()
        testInstance.sayHello = MagicMock(return_value=3)
        self.assertEqual(testInstance.sayHello(), 3)

    def test_mockIgnoreCheck(self):
        # type ignore comment allow to not break the mypy check
        # self.test_mockIgnoreCheck = MagicMock(return_value=True)  # type: ignore
        pass
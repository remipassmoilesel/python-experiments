import unittest
from unittest.mock import MagicMock


class SetupTest(unittest.TestCase):

    def setUp(self) -> None:
        """This method will be excuted before each test method"""
        super().setUp()

        self.exampleMock1 = MagicMock()

    def test_mock1(self):
        self.exampleMock1()
        self.exampleMock1.assert_called_once()

    def test_mock2(self):
        self.exampleMock1()
        self.exampleMock1.assert_called_once()

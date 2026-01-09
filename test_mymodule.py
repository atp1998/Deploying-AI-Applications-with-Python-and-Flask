import unittest

from mymodule import square, doubler

class TestSquare(unittest.TestCase):

    def test1(self):
        self.assertEqual(square(2), 4)

class TestDouble(unittest.TestCase):

    def test(self):
        self.assertEqual(doubler(2),4)


unittest.main()
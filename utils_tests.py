import unittest

from utils import utils

class TestUtils(unittest.TestCase):
    
    # Reversed Tests
    def test_r_int1(self):
        result = utils.reversed(4065)
        self.assertEqual(result, 5604)

    def test_r_int2(self):
        result = utils.reversed(385279)
        self.assertEqual(result, 972583)

    def test_r_str(self):
        result = utils.reversed("hello")
        self.assertEqual(result, None)

    def test_r_fl(self):
        result = utils.reversed(45.7)
        self.assertEqual(result, None)

    def test_r_str_int(self):
        result = utils.reversed("264")
        self.assertEqual(result, None)

    # Formatter Tests
    
    def test_f_int1(self):
        result = utils.formatter(170)
        self.assertEqual(result, (0b10101010, 0o252))

    def test_f_int2(self):
        result = utils.formatter(38)
        self.assertEqual(result, (0b100110, 0o46))

    def test_f_str(self):
        result = utils.formatter("hello")
        self.assertEqual(result, (None, None))

    def test_f_fl(self):
        result = utils.formatter(45.7)
        self.assertEqual(result, (None, None))

    def test_f_str_int(self):
        result = utils.formatter("264")
        self.assertEqual(result, (None, None))



if __name__ == '__main__':
    unittest.main()


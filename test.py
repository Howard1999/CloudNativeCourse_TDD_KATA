import unittest

from price import price


class TestPriceFunction(unittest.TestCase):
    
    def test_buy_one(self):
        self.assertEqual(8, price([0]))
        self.assertEqual(8, price([1]))
        self.assertEqual(8, price([2]))
        self.assertEqual(8, price([3]))
        self.assertEqual(8, price([4]))


if __name__ == '__main__':
    unittest.main()
    
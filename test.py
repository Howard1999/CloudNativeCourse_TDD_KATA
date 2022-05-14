import unittest

from price import price


class TestPriceFunction(unittest.TestCase):
    
    def test_buy_one(self):
        self.assertEqual(8, price([0]))
        self.assertEqual(8, price([1]))
        self.assertEqual(8, price([2]))
        self.assertEqual(8, price([3]))
        self.assertEqual(8, price([4]))

    def test_buy_same_book(self):
        self.assertEqual(8* 2, price([0, 0]))
        self.assertEqual(8* 3, price([1, 1, 1]))
        self.assertEqual(8* 4, price([2, 2, 2, 2]))
        self.assertEqual(8*10, price([4]*10))

if __name__ == '__main__':
    unittest.main()
    
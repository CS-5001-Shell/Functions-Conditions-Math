import unittest
from bill_splitter import get_per_diner_amount

class BillSplitterTest(unittest.TestCase):

    def test_bill_splitter_fair(self):
        self.assertAlmostEqual(47.2, get_per_diner_amount(80, 'fair', 2))

    def test_bill_splitter_good(self):
        self.assertAlmostEqual(60, get_per_diner_amount(100, 'good', 2))

    def test_bill_splitter_excellent(self):
        self.assertAlmostEqual(71.88, get_per_diner_amount(230, 'excellent', 4))

    def test_bill_splitter_bad_qos(self):
        self.assertAlmostEqual(-1, get_per_diner_amount(230, 'purple', 4))

if __name__ == '__main__':
    unittest.main()
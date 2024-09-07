import unittest
from electric_bill import calculate_bill

class ElectricBillTest(unittest.TestCase):

    def test_electric_bill_no_overage(self):
        self.assertEqual(200, calculate_bill(.25, 800))

    def test_electric_bill_with_overage(self):
        self.assertEqual(183.75, calculate_bill(.14, 1250))

    def test_electric_bill_exactly_at_overage(self):
        self.assertEqual(100, calculate_bill(.10, 1000))

if __name__ == '__main__':
    unittest.main()
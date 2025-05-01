import unittest
from tools.finance_tools import (
    calculate_emi, calculate_sip, calculate_fd, calculate_rd,
    calculate_retirement, calculate_home_loan_eligibility,
    calculate_credit_card_interest, calculate_taxable_income,
    calculate_budget, calculate_net_worth
)

class TestFinanceTools(unittest.TestCase):

    def test_calculate_emi_normal(self):
        # EMI calculation for ₹100,000 at 12% annual over 12 months
        emi = calculate_emi(principal=100000, annual_rate=12, months=12)
        self.assertAlmostEqual(8884.88, emi, places=2)

    def test_calculate_emi_zero_rate(self):
        emi = calculate_emi(principal=12000, annual_rate=0, months=12)
        self.assertEqual(1000.00, emi)

    def test_calculate_emi_invalid(self):
        with self.assertRaises(ValueError):
            calculate_emi(principal=-1, annual_rate=5, months=12)

    def test_calculate_sip_normal(self):
        sip = calculate_sip(monthly_investment=5000, annual_rate=8, months=12)
        self.assertTrue(isinstance(sip, float) and sip > 60000)

    def test_calculate_sip_invalid(self):
        with self.assertRaises(ValueError):
            calculate_sip(monthly_investment=1000, annual_rate=8, months=0)

    def test_calculate_fd(self):
        fd = calculate_fd(principal=10000, annual_rate=5, years=2)
        self.assertAlmostEqual(11025.00, fd, places=2)

    def test_calculate_rd(self):
        rd = calculate_rd(monthly_deposit=1000, annual_rate=6, months=12)
        self.assertTrue(isinstance(rd, float) and rd > 12000)

    def test_other_calculators(self):
        # retirement
        ret = calculate_retirement(10000, 1000, 5, 1)
        self.assertTrue(ret > 11000)
        # home loan eligibility
        elig = calculate_home_loan_eligibility(50000, 20000, 60)
        self.assertEqual((50000-20000)*60, elig)
        # credit card interest
        ic = calculate_credit_card_interest(balance=1000, annual_rate=12)
        self.assertTrue(ic > 0)
        # taxable income
        ti = calculate_taxable_income(90000, 10000)
        self.assertEqual(80000.00, ti)
        # budget planner
        b = calculate_budget(5000, 3000)
        self.assertEqual({'surplus': 2000.00, 'expense_ratio': 60.0, 'is_deficit': False}, b)
        # net worth
        nw = calculate_net_worth(100000, 50000)
        self.assertEqual(50000.00, nw)

if __name__ == "__main__":
    unittest.main()

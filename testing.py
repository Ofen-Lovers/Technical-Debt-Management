import unittest
from salaryDeduction import compute_deductions  # Replace 'your_module_name' with the actual filename (without .py)

class TestComputeDeductions(unittest.TestCase):

    def test_lowest_salary(self):
        """Test case for salary below SSS exemption threshold (e.g., 8000)"""
        sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(8000)
        self.assertEqual(sss, 0)  # SSS should be 0 for salary < 8250
        self.assertEqual(tax, 0)  # Tax should be 0 for salary < 25000
        self.assertGreater(net_salary, 0)  # Net salary should be positive

    def test_minimum_taxable_salary(self):
        """Test case for salary just below tax threshold (e.g., 24000)"""
        sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(24000)
        self.assertEqual(tax, 0)  # Tax should be 0
        self.assertGreater(net_salary, 0)  # Net salary should be positive

    def test_taxable_salary(self):
        """Test case for salary just above tax threshold (e.g., 25000)"""
        sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(25000)
        self.assertEqual(sss, 1200)  # SSS should be deducted
        self.assertEqual(tax, 1875)  # Tax should be deducted

    def test_high_salary(self):
        """Test case for a high salary (e.g., 100000)"""
        sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(100000)
        self.assertEqual(sss, 1200)  # SSS still applies
        self.assertEqual(tax, 1875)  # Fixed tax applied

    def test_negative_salary(self):
        """Test case for negative salary"""
        with self.assertRaises(ValueError):
            compute_deductions(-5000)

    def test_zero_salary(self):
        """Test case for zero salary"""
        sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(0)
        self.assertEqual(sss, 0)  # No SSS
        self.assertEqual(tax, 0)  # No tax
        self.assertEqual(deductions, 100)  # Only Pag-IBIG applies
        self.assertEqual(net_salary, -100)  # Net salary should reflect deductions

    def test_salary_at_sss_threshold(self):
        """Test case for salary at the SSS exemption threshold (e.g., 8250)"""
        sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(8250)
        self.assertEqual(sss, 1200)  # SSS applies
        self.assertEqual(tax, 0)  # Tax should still be 0

    def test_salary_at_tax_threshold(self):
        """Test case for salary at the tax threshold (e.g., 25000)"""
        sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(25000)
        self.assertEqual(tax, 1875)  # Tax applies

    def test_large_salary(self):
        """Test case for very high salary (e.g., 500000)"""
        sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(500000)
        self.assertEqual(sss, 1200)  # SSS fixed
        self.assertEqual(tax, 1875)  # Fixed tax applied

    def test_float_salary(self):
        """Test case for salary with decimal value"""
        sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(25500.75)
        self.assertEqual(sss, 1200)  # SSS applied
        self.assertEqual(tax, 1875)  # Tax applied

if __name__ == '__main__':
    unittest.main()

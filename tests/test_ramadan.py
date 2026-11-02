# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
from datetime import date
import unittest
from ramadanCalculator import ESTIMATES, days_until, result

class RamadanTests(unittest.TestCase):
    def test_days(self):
        self.assertEqual(days_until(date(2026, 2, 18), date(2026, 2, 17)), 1)
        self.assertEqual(days_until(date(2026, 2, 18), date(2026, 2, 19)), -1)
    def test_two_2030_estimates(self):
        self.assertIn("2030 (first)", ESTIMATES)
        self.assertIn("2030 (second)", ESTIMATES)
    def test_result(self):
        self.assertIn("1 days remaining", result("2026", date(2026, 2, 17)))
    def test_unknown(self):
        with self.assertRaises(ValueError):
            result("2040")

if __name__ == "__main__":
    unittest.main()

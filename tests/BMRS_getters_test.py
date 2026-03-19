import unittest
from Daily_report import BMRS_getters as bmrs

SETTLEMENT_DATE = "2023-01-02"

class TestBMRSGetters(unittest.TestCase):
    def test_get_b1770_day(self):
        """
        Test that get_b1770_day returns a DataFrame with correct columns and 48 rows.
        """
        df = bmrs.get_b1770_day(SETTLEMENT_DATE)
        expected_cols = ["Settlement Period", "ImbalancePriceAmount"]
        self.assertEqual(list(df.columns), expected_cols)
        self.assertEqual(len(df), 48)

    def test_get_b1780_day(self):
        """
        Test that get_b1780_day returns a DataFrame with correct columns and 48 rows.
        """
        df = bmrs.get_b1780_day(SETTLEMENT_DATE)
        expected_cols = ["Settlement Period", "Imbalance Quantity (MAW)"]
        self.assertEqual(list(df.columns), expected_cols)
        self.assertEqual(len(df), 48)

if __name__ == "__main__":
    unittest.main()

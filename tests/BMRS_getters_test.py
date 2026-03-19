from unittest import TestCase
import Daily_report.BMRS_getters as bmrs

version_number = "v1"  # v1 or V1 (case-insensitive)
service_type = "csv"  # csv or xml
settlement_date = "2023-01-02"


class TestGetB1770Day(TestCase):
    def test_get_b1770_day(self):
        """
        tests the column names and number of rows of the dataframe returned by get_b1770_day

        :return:
        """
        b1770_known_cols = ['*DocumentID', 'DocumentRevNum', 'ActiveFlag', 'ProcessType', 'DocumentType', 'Resolution',
                            'CurveType', 'PriceCategory', 'ImbalancePriceAmount', 'SettlementPeriod', 'SettlementDate',
                            'ControlArea', 'BusinessType', 'TimeSeriesID', 'DocumentStatus']
        rm_list = ['PriceCategory', 'TimeSeriesID']
        df = bmrs.get_b1770_day(settlement_date)
        # test column names
        self.assertEqual(set(df.columns), set(b1770_known_cols).difference(rm_list))
        # test number of rows
        self.assertEqual(len(df), 48)


class TestGetB1780Day(TestCase):
    def test_get_b1780_day(self):
        """
        tests the column names and number of rows of the dataframe returned by get_b1780_day

        :return:
        """
        b1780_known_cols = ['*Time Series ID', 'Business Type', 'Control Area', 'Settlement Date', 'Settlement Period',
                            'Imbalance Quantity (MAW)', 'Curve Type', 'Resolution', 'Document Type', 'Process Type',
                            'Active Flag', 'Document Status', 'Document ID', 'Document RevNum',
                            'Imbalance Quantity Direction']
        df = bmrs.get_b1780_day(settlement_date)
        # test column names
        self.assertEqual(set(df.columns), set(b1780_known_cols))
        # test number of rows
        self.assertEqual(len(df), 48)

import unittest
from functionality.csv_formatter import CSV_Formatter


class Test_CSV_Formatting(unittest.TestCase):
    def test_csv_format(self):
        self.assertTrue(CSV_Formatter().format_range_to_csv([[4, 5]]) == "Range, Readings\n4-5, 2")


if __name__ == '__main__':
    unittest.main()

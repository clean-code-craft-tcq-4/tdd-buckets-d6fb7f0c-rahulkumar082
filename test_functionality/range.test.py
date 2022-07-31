import unittest
from functionality.range import Range


class TestRange(unittest.TestCase):
    def test_input_types(self):
        self.assertTrue(Range().sort_input_int_arr([2, 3, 100, 53, 433, 343]) == [2, 3, 53, 100, 343, 433])
        self.assertTrue(Range().sort_input_int_arr([2, 3, 100, 53, 433, 34.3]) == 'NOT_INT')

    def test_periodic_range(self):
        self.assertTrue(Range().periodic_intervals([4, 5]) == [4, 5])
        self.assertTrue(Range().periodic_intervals([3, 3, 4, 5, 10, 11, 12]) == [3, 3, 4, 5, 'Interval', 10, 11, 12])

    def test_list_of_periodic_range(self):
        self.assertTrue(Range().list_of_periodic_ranges(
            [3, 3, 4, 5, 'Interval', 10, 11, 12]) == [[3, 3, 4, 5], [10, 11, 12]])
        self.assertTrue(Range().list_of_periodic_ranges([4, 5]) == [[4, 5]])

    def test_range_list(self):
        self.assertTrue(Range().get_range_list([3, 3, 4, 5, 10, 11, 12]) == [[3, 3, 4, 5], [10, 11, 12]])


if __name__ == '__main__':
    unittest.main()

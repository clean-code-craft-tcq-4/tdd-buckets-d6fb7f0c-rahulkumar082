import unittest
from bms_factors.samples.current.current_sample import CurrentSample


class Test_Current_Sample(unittest.TestCase):
    def test_periodic_current(self):
        self.assertTrue(CurrentSample().periodic_current_range([5, 4]) == 'Range, Readings\n4-5, 2')
        self.assertTrue(CurrentSample().periodic_current_range(
            [3, 3, 5, 4, 10, 11, 12]) == 'Range, Readings\n3-5, 4\n10-12, 3')
    def test_not_applicable_current(self):
        self.assertTrue(CurrentSample().periodic_current_range([3, 3.5, 4, 23]) == 'NOT_APPLICABLE')


if __name__ == '__main__':
    unittest.main()

import unittest
from bms_factors.samples.current.current_sample import CurrentSample


class Test_Current_Sample(unittest.TestCase):
    def test_periodic_currentin_amps(self):
        self.assertTrue(CurrentSample().periodic_current_range_in_amps([5, 4]) == 'Range, Readings\n4-5, 2')
        self.assertTrue(CurrentSample().periodic_current_range_in_amps(
            [3, 3, 5, 4, 10, 11, 12]) == 'Range, Readings\n3-5, 4\n10-12, 3')

    def test_not_applicable_current(self):
        self.assertEqual(CurrentSample().periodic_current_range_in_amps([3, 3.5, 4, 23]), 'NOT_APPLICABLE')

    def test_a2d_current(self):
        self.assertEqual(CurrentSample().periodic_current_range_in_12_bits([0, 1000, 1147, 1148]), 'Range, Readings\n0-0, 1\n2-3, 3')



if __name__ == '__main__':
    unittest.main()

import unittest
from range import Range

class TestRange(unittest.TestCase):
    def test_input_types(self):
        self.assertTrue(Range().sort_input_int_arr([2,3,100,53,433,343]) == [2,3,53,100,343,433])
        self.assertTrue(Range().sort_input_int_arr([2,3,100,53,433,34.3]) == 'NOT_INT')


if __name__ == '__main__':
    unittest.main()
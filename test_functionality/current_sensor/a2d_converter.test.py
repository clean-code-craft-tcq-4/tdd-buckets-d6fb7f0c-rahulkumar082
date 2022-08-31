import unittest
from functionality.current_sensor.a2d_converter import A2D_Converter

class Test_A2D_Converter(unittest.TestCase):
    def test_single_value_conversion(self):
        self.assertEqual(A2D_Converter().map_value(4094), 10)
        self.assertEqual(A2D_Converter().map_value(4095), 'Error_Reading')
        self.assertEqual(A2D_Converter().map_value(-1), 'Error_Reading')

if __name__ == '__main__':
    unittest.main()
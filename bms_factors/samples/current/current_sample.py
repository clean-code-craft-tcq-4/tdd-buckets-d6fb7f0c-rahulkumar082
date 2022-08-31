from distutils.log import error
from functionality.utils.range import Range
from functionality.utils.csv_formatter import CSV_Formatter
from functionality.current_sensor.a2d_converter import A2D_Converter


class CurrentSample:
    def __init__(self) -> None:
        self.range_obj = Range()
        self.csv_obj = CSV_Formatter()
        self.a2d_obj = A2D_Converter()

    def periodic_current_range_in_amps(self, current_sample):
        range_list_with_count = self.range_obj.get_range_list(current_sample)
        if ('NOT_INT' not in range_list_with_count):
            return self.csv_obj.format_range_to_csv(range_list_with_count)
        return 'NOT_APPLICABLE'

    def periodic_current_range_in_12_bits(self, current_sample):
        amps_readings_list = []
        for reading in current_sample:
            value = self.a2d_obj.map_value(reading)
            if (value is not 'Error_Reading'):
                amps_readings_list.append(value)
        return self.periodic_current_range_in_amps(amps_readings_list)

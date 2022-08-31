from distutils.log import error
from functionality.range import Range
from functionality.csv_formatter import CSV_Formatter


class CurrentSample:
    def __init__(self) -> None:
        self.range_obj = Range()
        self.csv_obj = CSV_Formatter()

    def periodic_current_range(self, current_sample):
        range_list_with_count = self.range_obj.get_range_list(current_sample)
        if ('NOT_INT' not in range_list_with_count):
            return self.csv_obj.format_range_to_csv(range_list_with_count)
        return 'NOT_APPLICABLE'

class Range:
    def get_range_list(self, arr):
        sorted_input = self.sort_input_int_arr(arr)
        if ('NOT_INT' not in sorted_input):
            periodic_range = self.periodic_intervals(sorted_input)
            periodic_range_list = self.list_of_periodic_ranges(periodic_range)
            return periodic_range_list
        return sorted_input

    def sort_input_int_arr(self, arr):
        is_int = all([isinstance(item, int) for item in arr])
        print(is_int)
        if is_int:
            arr.sort()
            return arr
        return 'NOT_INT'

    def periodic_intervals(self, sorted_arr):
        periodic_interval_range = []
        sorted_arr_length = len(sorted_arr)
        range_interval = 1
        for index in range(0, sorted_arr_length):
            if (sorted_arr[index] > sorted_arr[index-1] + range_interval):
                periodic_interval_range.append('Interval')
            periodic_interval_range.append(sorted_arr[index])
        return periodic_interval_range

    def list_of_periodic_ranges(self, periodic_interval_range):
        periodic_interval_range.append('Interval')
        list_of_ranges = []
        temp_arr = []
        for item in periodic_interval_range:
            if (item != 'Interval'):
                temp_arr.append(item)
            else:
                list_of_ranges.append(temp_arr)
                temp_arr = []
                continue
        return list_of_ranges

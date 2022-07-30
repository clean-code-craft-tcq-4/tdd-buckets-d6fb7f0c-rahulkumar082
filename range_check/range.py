class Range:
    def sort_input_int_arr(self, arr):
        is_int = all([isinstance(item, int) for item in arr])
        print(is_int)
        if is_int:
            arr.sort()
            return arr
        return 'NOT_INT'

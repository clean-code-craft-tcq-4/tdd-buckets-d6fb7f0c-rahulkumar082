class CSV_Formatter:
    def format_range_to_csv(self, range_list):
        csv_string_list = []
        complete_csv_string = ""
        csv_string_list.append(self.csv_headers())
        for list_item in range_list:
            csv_string_list.append(self.first_and_last_element_with_count(list_item))
        complete_csv_string = "\n".join(csv_string_list)
        return complete_csv_string

    def first_and_last_element_with_count(self, nested_list):
        count = len(nested_list)
        first_element = nested_list[0]
        last_element = nested_list[-1]
        return f"{first_element}-{last_element}, {count}"

    def csv_headers(self):
        return f"Range, Readings"


if __name__ == '__main__':
    CSV_Formatter().format_range_to_csv([[4, 5]])

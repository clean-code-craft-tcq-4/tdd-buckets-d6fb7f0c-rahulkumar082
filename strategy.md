# Strategy to solve the problem

## Requirements
* Take integer array as input. Assuming it could be in jumbled order.
* Sort the integer array and differentiate the continuous range
    * In sorted integer array, if diff between two integer is greater than 1, it should be in different ranges
    * E.g. in [3, 3, 4, 5, 10, 11, 12], 10 - 5 > 1 and hence it acts as **divider** for the ranges
        * Therefore, [3 - 5] and [10 - 12] are seperate ranges
* Count the number of elements in each range
* Output in csv format:
    * `<range>`, `<number of element>`

## Tests
* Test the integer array acceptance input, in case float input is given, return error
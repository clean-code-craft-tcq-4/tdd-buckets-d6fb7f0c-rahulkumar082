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

## Technical aspects
* **functionality**:
    * range:
        * It takes the integer array as input and sorts it
        * It creates ranges in the respective array (a trick I have used here is that in case the numbers differs more than 1, put *'Interval'*)
        * With each 'Interval' occurance, split the array into multiple ranges
    * csv_formatter:
        * From nested range lists, it counts the elements in each list and gives output in csv format
* **bms_factors/samples/current**: a folder where we can keep other bms influencing factors such as current, temperatures etc.
    * Current: It uses both *range* and *csv_formatter* functionality and
        * Takes input as integer array
        * Gives output in csv format as *Range, Readings*


**Note**: Folder structure of bms_factors should ensure simple refactors if more parameters such as temperature, charge state are added.

## Tests
* **functionality**:
    * range:
        * Test the type of inputs (should be int) and sorted output
        * Test the lists having 'Intervals' at right places
        * Test the split of bigger list into 'Interval' bounded small lists. In case no 'Interval' found, it would mean all elements belong to same array
        * Test the combined effect of above with just one array
    * csv_formatter:
        * Test if the CSV formatter works properly with one dummy input and expected output with headings (Range, Readings)
* **bms_factors/samples/current**:
    * CurrentSample:
        * Give an input array and test if the output lies in correct range with headers

**Note**: I believe there could be less time-and-space complex algorithms which can accomplish this task much easier and quick way, suggestions are most welcome. :)


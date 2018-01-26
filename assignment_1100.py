'''
Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.
The numbers can appear anywhere in the line. 
There can be any number of numbers in each line (including none).

Desired output:
regex_sum.txt : 445833
regex_sum_1.txt : 466318

'''


import re

# Ask the user for the file name and open the file
file_name = input("Please enter the file name:")

# Providing a default file name
if len(file_name)<1: file_name = 'regex_sum_test.txt'

# Extracting the numbers from the file and summing them (using list comprehension)
print(sum([int(num) for num in re.findall('[0-9]+',open(file_name, 'r').read())]))

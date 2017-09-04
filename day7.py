#!/bin/python3

# convert string array to int array vice verca

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

rev = [str(item) for item in reversed(arr)]

print(" ".join(rev))
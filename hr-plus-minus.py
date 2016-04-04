#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

num_pos = 0
num_neg = 0
num_zero = 0

for val in arr:
    if val > 0:
        num_pos += 1
    elif val < 0:
        num_neg += 1
    else:
        num_zero += 1

total = num_pos + num_neg + num_zero
print('%.6f\n%.6f\n%.6f' % ((float(num_pos) / total), (float(num_neg) / total), (float(num_zero) / total)))

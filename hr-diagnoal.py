#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)

first_diagonal = 0
second_diagonal = 0


for i in range(n):
    first_diagonal += a[i][i]
    second_diagonal += a[i][n-i-1]


print(abs(first_diagonal - second_diagonal))

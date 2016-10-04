#!/bin/python3


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)


def hourglass_sum(i, j):
    return arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i][j] + arr[i + 1][j - 1] + arr[i + 1][j] + \
           arr[i + 1][j + 1]


max_sum = -100
for i in range(1, 5):
    for j in range(1, 5):
        sum = hourglass_sum(i, j)
        if sum > max_sum:
            max_sum = sum

print(max_sum)

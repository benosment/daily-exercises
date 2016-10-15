#!/bin/python3


def bubble(l):
    total_swaps = 0
    for i in range(len(l)):
        num_swaps = 0
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                num_swaps += 1
                total_swaps += 1
        if num_swaps == 0:
            return l, total_swaps
    return l, total_swaps


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
l, total_swaps = bubble(a)

print('Array is sorted in %d swaps.' % total_swaps)
print('First Element: %d' % l[0])
print('Last Element: %d' % l[-1])

#! /usr/bin/env python3


def mark_and_toys(l, budget):
    '''
     l - list of prices of toys
     budget - total amount left for toys
    '''
    bought = []
    while l and (min(l) <= budget):
        item = min(l)
        bought.append(item)
        l.remove(item)
        budget = budget - item
    return len(bought)


n, budget = input().strip().split(' ')
budget = int(budget)
items = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(mark_and_toys(items, budget))

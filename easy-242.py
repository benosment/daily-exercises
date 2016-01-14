#! /usr/bin/env python3

'''
[Description]
Scientist have discovered a new plant. The fruit of the
plant can feed 1 person for a whole week and best of all, the plant
never dies. Fruits needs 1 week to grow, so each weak you can harvest
it fruits. Also the plant gives 1 fruit more than the week before and
to get more plants you need to plant a fruit.  Now you need to
calculate after how many weeks, you can support a group of x people,
given y fruits to start with.

Input: 15 1
Output: 5

[Input description]
The input gives you 2 positive integers x and y, being x the number of
people needed to be fed and y the number of fruits you start with.

[Output description]
The number of weeks before you can feed the entire group of people.
'''

import argparse


def calc_total(l):
    total = 0
    mult = 0
    for elem in l:
        total += elem * mult
        mult += 1
    return total


def calc_total_plants(l):
    total = 0
    mult = 1
    for elem in l:
        total += elem * mult
        mult += 1
    return total


def fruit(need, plant_list, day):
    total = calc_total(plant_list)
    print(need, plant_list, day, total)
    if total > need:
        return day + 1
    plant_list.insert(0, calc_total_plants(plant_list))
    return fruit(need, plant_list, day+1)


def plant(people, plants):
    weeks = 0
    fruits = 0
    while fruits < people:
        print(people, fruits, plants, weeks)
        weeks += 1
        fruits += plants
        plants += fruits
    return weeks + 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='easy 242')
    parser.add_argument('num_people', action='store',
                        help='number of people that need to be fed')
    parser.add_argument('num_plants', action='store',
                        help='number of plants you start with')
    args = parser.parse_args()
    print(plant(int(args.num_people), int(args.num_plants)))

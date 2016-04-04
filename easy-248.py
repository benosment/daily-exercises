#! /usr/bin/env python3

import random

def ss():
    families = []
    mapping = {}

    with open('easy-248.txt') as f:
        for line in f.readlines():
            families.append(line.split())

    families.sort(key = lambda x: -len(x))
    recip = []
    for family in families:
        recip.append(family[:])

    for (i, family) in enumerate(families):
        for person in family:
            # select a family
            other_families = list(range(len(recip)))
            other_families.remove(i)
            random_family = random.choice(other_families)
            fail_count = 0
            while len(recip[random_family]) == 0:
                if fail_count > len(families):
                    return {}
                random_family = random.choice(other_families)
            # select a member within that family
            random_member = random.choice(recip[random_family])

            mapping[person] = random_member
            # remove from recip list
            recip[random_family].remove(random_member)
    return mapping


if __name__ == '__main__':
    mapping = ss()
    while not mapping:
        mapping = ss()
    for key in mapping.keys():
        print('%s -> %s' % (key, mapping[key]))

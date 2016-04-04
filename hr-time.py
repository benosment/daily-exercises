#!/bin/python3

import sys


time = input().strip()
h,m,s = time.split(':')
am_pm = s[2:]
s = s[:2]
h = int(h)
if am_pm == 'PM':
    if (h != 12):
        h += 12
    print('%d:%s:%s' % (h, m, s))
else:
    if (h == 12):
        h = 0
    if (h < 10):
        h = '0%d' % h
    else:
        h = str(h)
    print('%s:%s:%s' % (h, m, s))

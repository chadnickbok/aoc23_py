#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()


inputs = lines[0].strip().split(",")

total = 0
for i in inputs:

    i = i.encode('utf-8')
    cur = 0

    for c in i:
        cur += c
        cur = cur * 17
        cur = cur % 256
    print(i, cur)
    total += cur
print(total)

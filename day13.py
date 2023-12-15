#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

blocks = []
cur = []

for line in lines:
    l = line.strip()
    if len(l) == 0:
        blocks.append(cur)
        cur = []
    else:
        cur.append(l)

blocks.append(cur)

print(len(blocks))

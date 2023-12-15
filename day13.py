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


def test_reflection(s, i):
    l = s[:i][::-1]
    r = s[i:]

    for i in range(0, min(len(l), len(r))):
        if l[i] != r[i]:
            return False
    return True


def reflects_horizontally(l, r):
    if len(l) != len(r):
        print("Sliced wrong!")

    for i, c in enumerate(r):
        if a[-i - 1] != c:
            return False
    return True


for block in blocks:
    possibles = []
    for i in range(1, len(block[0]) - 1):
        possibles.append(i)
    for _, l in enumerate(block):
        cur_possibles = []
        for i in possibles:
            if test_reflection(l, i):
                cur_possibles.append(i)
        possibles = cur_possibles
    
    if len(possibles) > 0:
        print(possibles)

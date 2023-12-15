#!/usr/bin/env python3

import sys
import json

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
    smudges = 0
    l = s[:i][::-1]
    r = s[i:]

    print(l, r)
    for i in range(0, min(len(l), len(r))):
        if l[i] != r[i]:
            smudges += 1
    return smudges


totals = 0

for block in blocks:
    possibles = []
    for i in range(1, len(block[0]) ):
        possibles.append(i)
    for _, l in enumerate(block):
        cur_possibles = []
        for i in possibles:
            if test_reflection(l, i) == 0:
                cur_possibles.append(i)
        possibles = cur_possibles
        print(possibles)
    
    if len(possibles) > 0:
        print(possibles)
        totals += possibles[0]
        continue

    rotated = []
    for i in range(0, len(block[0])):
        rotated.append([])

    for j in range(0, len(block)):
        for i in range(0, len(block[0])):
            rotated[i].append(block[j][i])

    possibles = []
    for i in range(1, len(rotated[0])):
        possibles.append(i)
    for _, l in enumerate(rotated):
        cur_possibles = []
        for i in possibles:
            if test_reflection(l, i) == 0:
                cur_possibles.append(i)
        possibles = cur_possibles
        print(possibles)

    if len(possibles) > 0:
        totals += possibles[0] * 100
    else:
        print("Broken block")
        for l in rotated:
            print(l)

print(totals)

totals = 0
for block in blocks:
    possibles = {}
    for i in range(1, len(block[0]) ):
        possibles[i] = 0
    for _, l in enumerate(block):
        for i in possibles:
            smudges = test_reflection(l, i)
            possibles[i] += smudges

    have_horizontal = False
    for possible in possibles:
        if possibles[possible] == 1:
            totals += possible
            have_horizontal = True
            break
    if have_horizontal:
        continue

    rotated = []
    for i in range(0, len(block[0])):
        rotated.append([])

    for j in range(0, len(block)):
        for i in range(0, len(block[0])):
            rotated[i].append(block[j][i])

    possibles = {}
    for i in range(1, len(rotated[0])):
        possibles[i] = 0

    for _, l in enumerate(rotated):
        for i in possibles:
            smudges = test_reflection(l, i)
            possibles[i] += smudges


    for possible in possibles:
        if possibles[possible] == 1:
            totals += possible * 100

print(totals)




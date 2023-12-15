#!/usr/bin/env python3

import sys
import json

with open(sys.argv[1]) as f:
    lines = f.readlines()

inputs = [line.strip().split() for line in lines]

def get_possibilities(s, sizes, count, cache):
    if len(s) == 0:
        # Reached the end of the string
        if len(sizes) == 0 and count == 0:
            # This is a possibility
            return 1
        else:
            # Dead end
            return 0

    if s[0] == "?":
        possible_chars = ["#", "."]
    else:
        possible_chars = [s[0]]

    n = 0
    for c in possible_chars:
        if c == "#":
            # Increase the current count and keep going
            n += get_possibilities(s[1:], sizes, count + 1, cache)
            continue

        if count != 0 and len(sizes) > 0 and count == sizes[0]:
            # Current group is good, keep going
            n += get_possibilities(s[1:], sizes[1:], 0, cache)
        elif count == 0:
            n += get_possibilities(s[1:], sizes, 0, cache)

    return n


total = 0
for t in inputs:
    s = t[0] + "."
    sizes = [int(x) for x in t[1].split(",")]

    p = get_possibilities(s, sizes, 0, {})
    print(s, sizes, p)
    total += p

print(total)

total = 0
for t in inputs:
    s = "?".join([t[0]] * 5) + "."
    sizes = [int(x) for x in t[1].split(",")] * 5

    p = get_possibilities(s, sizes, 0, {})
    print(s, sizes, p)
    total += p
print(total)

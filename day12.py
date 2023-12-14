#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()


def is_valid(s, runs):
    counts = []
    cur = s[0]
    count = 0
    for c in s[1:]:
        if cur == "#":
            count += 1
        elif count > 0:
            counts.append(count)
            count = 0
        cur = c

    if cur == "#":
        count += 1
    if count > 0:
        counts.append(count)

    if len(counts) != len(runs):
        #print("len counts:", len(counts), "len runs:", len(runs))
        return False

    for i, count in enumerate(counts):
        if count != runs[i]:
            #print(counts, runs)
            return False
    return True


def get_positions(s, runs):
    i = s.find('?')
    if i >= 0:
        return get_positions(s[:i] + "." + s[i+1:], runs) + get_positions(s[:i] + "#" + s[i+1:], runs)

    if is_valid(s, runs):
        #print(s, "Valid")
        return 1
    else:
        #print(s, "Invalid")
        return 0


total = 0
for line in lines:
    parts = line.strip().split()
    springs = parts[0]
    runs = [int(x) for x in parts[1].split(",")]

    valid_positions = get_positions(springs, runs)
    total += valid_positions
print(total)

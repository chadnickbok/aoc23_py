#!/usr/bin/env python3

import sys


def find_differences(vals):
    diffs = []
    for i in range(0, len(vals) - 1):
        diffs.append(vals[i + 1] - vals[i])
    return diffs


def is_all_zeros(vals):
    for val in vals:
        if val != 0:
            return False
    return True


with open(sys.argv[1]) as f:
    lines = f.readlines()

next_vals = []
for line in lines:
    vals = [int(x) for x in line.strip().split()]

    diffs = [find_differences(vals)]
    while not is_all_zeros(diffs[-1]):
        diffs.append(find_differences(diffs[-1]))
        print(diffs)

    diffs.reverse()

    next_val = 0
    for diff in diffs:
        next_val += diff[-1]

    print(vals[-1] + next_val)
    next_vals.append(vals[-1] + next_val)

print(sum(next_vals))

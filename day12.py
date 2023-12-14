#!/usr/bin/env python3

import sys
import re

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


def is_already_invalid(s, runs):
    total_hashes = sum(runs)
    cur_potential_hashes = s.count("#") + s.count("?")

    if cur_potential_hashes < total_hashes:
        return True

    pattern = "[\.\?]*"
    for run in runs:
        pattern += f"[#\?]{{{run}}}[\.\?]*"
    r = re.compile(pattern)

    if r.search(s) is None:
        #print(s, pattern)
        return True

    cur_s = s[:s.find("?")]

    counts = []
    cur = s[0]
    count = 0

    for c in cur_s[1:]:
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

    if len(counts) == 0:
        return False

    if len(counts) > len(runs):
        return True

    for i in range(0, len(counts) - 1):
        if counts[i] != runs[i]:
            return True

    if counts[-1] > runs[len(counts) - 1]:
        return True

    return False


def get_positions(s, runs):

    i = s.find('?')
    if i >= 0:
        if is_already_invalid(s, runs):
            return 0
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

total = 0
for line in lines:
    parts = line.strip().split()
    springs = parts[0]
    runs = [int(x) for x in parts[1].split(",")]

    print(springs)
    
    expanded_springs = []
    expanded_runs = []
    for i in range(0, 5):
        expanded_runs += runs
        expanded_springs.append(springs)
    expanded_springs = "?".join(expanded_springs)

    valid_positions = get_positions(expanded_springs, expanded_runs)
    total += valid_positions

print(total)

#!/usr/bin/env python3

import sys
import json

def parse_card(line):
    card_parts = line.split(":")[1].split("|")
    winning_numbers = card_parts[0].strip().split()
    numbers_you_have = card_parts[1].strip().split()

    score = 0
    for n in numbers_you_have:
        if n in winning_numbers:
            score += 1
    return score


with open(sys.argv[1]) as f:
    lines = f.readlines()


counts = {0: 1}
for i in range(0, len(lines)):
    if i not in counts:
        counts[i] = 1
    cur_count = counts[i]

    c = parse_card(lines[i].strip())

    for j in range(0, c):
        cur_card = i + j + 1
        if cur_card in counts:
            counts[cur_card] += cur_count
        else:
            counts[cur_card] = cur_count + 1

print(json.dumps(counts, indent=2))
print(sum(counts.values()))

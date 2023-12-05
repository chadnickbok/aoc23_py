#!/usr/bin/env python3

import sys

def parse_card(line):
    card_parts = line.split(":")[1].split("|")
    winning_numbers = card_parts[0].strip().split()
    numbers_you_have = card_parts[1].strip().split()

    score = 0
    for n in numbers_you_have:
        if n in winning_numbers:
            if score == 0:
                score = 1
            else:
                score = score * 2
    return score


with open(sys.argv[1]) as f:
    lines = f.readlines()

scores = []
for line in lines:
    score = parse_card(line.strip())
    print(score)
    scores.append(score)

print(sum(scores))

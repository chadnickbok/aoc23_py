#!/usr/bin/env python3

import re

with open("day3.txt") as f:
    lines = f.readlines()

part_numbers = []
for i in range(0, len(lines)):
    for m in re.finditer("\d+", lines[i]):
        start = m.start()
        end = m.end()

        l = start - 1
        if l < 0:
            l = 0
        r = end + 2
        if r > len(lines[0]):
            r = len(lines[0])
        up = i - 1
        if up < 0:
            up = 0

        down = i + 2
        if down > len(lines):
            down = len(lines)

        is_part_number = False
        for y in range(up, down):
            for x in range(l, r):
                if not lines[y][x].isdigit() and not lines[y][x] == ".":
                    is_part_number = True

        if is_part_number:
            part_numbers.append(int(m.group()))
        print(m.group(), l, r, up, down, is_part_number)

#print(part_numbers)
print(sum(part_numbers))
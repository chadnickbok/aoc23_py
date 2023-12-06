#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

stripped_lines = []
for line in lines:
    stripped_lines.append(line.strip())

lines = stripped_lines

gears = {}
part_numbers = []
for i in range(0, len(lines)):
    for m in re.finditer("\d+", lines[i]):
        start = m.start()
        end = m.end()

        l = start - 1
        if l < 0:
            l = 0
        r = end + 1
        if r > len(lines[0]):
            r = len(lines[0])
        up = i - 1
        if up < 0:
            up = 0

        down = i + 2
        if down > len(lines):
            down = len(lines)

        is_part_number = False
        cur_gears = set()
        for y in range(up, down):
            for x in range(l, r):
                if lines[y][x] == "*":
                    loc = (y, x)
                    cur_gears.add(loc)

        v = int(m.group())
        for gear in cur_gears:
            if gear in gears:
                gears[gear].append(v)
            else:
                gears[gear] = [v]

gear_ratios = []
for g in gears.values():
    if len(g) == 2:
        gear_ratios.append(g[0] * g[1])

print(sum(gear_ratios))

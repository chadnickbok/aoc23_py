#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

expanded_v_lines = []

# Expand all the lines vertically
for line in lines:
    l = line.strip()

    empty = True
    for c in l:
        if c == "#":
            empty = False
            break

    expanded_v_lines.append(l)
    if empty:
        expanded_v_lines.append(l)

print("Expanded vertically")
for line in expanded_v_lines:
    print("".join(line))

empty_cols = []
for i in range(0, len(lines[0])):
    is_empty = True
    for j in range(0, len(lines)):
        if lines[j][i] == "#":
            is_empty = False
            break

    if is_empty:
        empty_cols.append(i)

expanded_lines = []
for line in expanded_v_lines:
    expanded_line = []
    for i in range(0, len(line)):
        expanded_line.append(line[i])
        if i in empty_cols:
            expanded_line.append(line[i])
    expanded_lines.append(expanded_line)


print("Expanded Horizontally")
for line in expanded_lines:
    print("".join(line))

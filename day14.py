#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

rocks = []
for line in lines:
    cur = []
    for c in line.strip():
        cur.append(c)
    rocks.append(cur)

print("start")
for line in rocks:
    print("".join(line))

# Go column-by-column
for i in range(0, len(rocks[0])):
    cur = 0
    next = 0

    # Now go row-by-row
    while next < len(rocks):
        if rocks[next][i] == "#":
            # Reset to the next position
            next += 1
            cur = next

        elif rocks[next][i] == "O":
            if cur != next:
                # Swap cur and next
                rocks[cur][i] = "O"
                rocks[next][i] = "."

            cur += 1
            next += 1

        else:
            next += 1

print("End")
for line in rocks:
    print("".join(line))

total = 0
for j in range(0, len(rocks)):
    cur = len(rocks) - j
    for i in range(0, len(rocks[0])):
        if rocks[j][i] == "O":
            total += cur
print(total)

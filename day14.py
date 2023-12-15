#!/usr/bin/env python3

import sys
import json

with open(sys.argv[1]) as f:
    lines = f.readlines()

rocks = []
for line in lines:
    cur = []
    for c in line.strip():
        cur.append(c)
    rocks.append(cur)


def tilt_rocks_north(rocks):
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


def tilt_rocks_west(rocks):
    # Go row-by-row
    for j in range(0, len(rocks)):
        cur = 0
        next = 0

        # Now go column-by-column
        while next < len(rocks[0]):
            if rocks[j][next] == "#":
                # Reset to the next position
                next += 1
                cur = next
            elif rocks[j][next] == "O":
                if cur != next:
                    # Swap cur and next
                    rocks[j][cur] = "O"
                    rocks[j][next] = "."
                cur += 1
                next += 1
            else:
                next += 1


def tilt_rocks_south(rocks):
    # Go column-by-column
    for i in range(0, len(rocks[0])):
        cur = len(rocks) - 1
        next = cur

        # Now go row-by-row
        while next >= 0:
            if rocks[next][i] == "#":
                # Reset to the next position
                next -= 1
                cur = next

            elif rocks[next][i] == "O":
                if cur != next:
                    # Swap cur and next
                    rocks[cur][i] = "O"
                    rocks[next][i] = "."

                cur -= 1
                next -= 1

            else:
                next -= 1


def tilt_rocks_east(rocks):
    # Go row-by-row
    for j in range(0, len(rocks)):
        cur = len(rocks[0]) - 1
        next = cur

        # Now go column-by-column
        while next >= 0:
            if rocks[j][next] == "#":
                # Reset to the next position
                next -= 1
                cur = next
            elif rocks[j][next] == "O":
                if cur != next:
                    # Swap cur and next
                    rocks[j][cur] = "O"
                    rocks[j][next] = "."
                cur -= 1
                next -= 1
            else:
                next -= 1


def copy_rocks(rocks):
    new_rocks = []
    for line in rocks:
        new_rocks.append(line.copy())
    return new_rocks


results = {}

print("start")
for line in rocks:
    print("".join(line))

key = json.dumps(rocks)

for i in range(0, 1000000000):
    if i % 1000000 == 0:
        print(i)

    if key in results:
        #print("Found key in results")
        (rocks, next_key) = results[key]
        key = next_key
    else:
        #print("Tilting")
        rocks = copy_rocks(rocks)
        tilt_rocks_north(rocks)
        tilt_rocks_west(rocks)
        tilt_rocks_south(rocks)
        tilt_rocks_east(rocks)

        next_key = json.dumps(rocks)
        results[key] = (rocks, next_key)
        key = next_key

    #print("State")
    #for line in rocks:
    #    print("".join(line))

total = 0
for j in range(0, len(rocks)):
    cur = len(rocks) - j
    for i in range(0, len(rocks[0])):
        if rocks[j][i] == "O":
            total += cur
print(total)

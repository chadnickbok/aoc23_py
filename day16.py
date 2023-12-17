#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

tiles = [line.strip() for line in lines]

def add_next(pos, dir):
    next_tiles.append({
        "pos": pos,
        "dir": dir
    })

# Energize the tile at (x, y), given a certain direction in 'u', 'd', 'l', 'r'
# Then figure out what the next direction to go in is.
def energize_tiles(pos, direction):
    # Check x is within bounds
    if pos[0] < 0 or pos[0] >= len(tiles[0]):
        return

    # Check y is within bounds
    if pos[1] < 0 or pos[1] >= len(tiles):
        return

    # Only go in a certain direction, from a starting point, once
    if (pos, direction) in direction_cache:
        return
    direction_cache.add((pos, direction))

    # Energize the current pos
    energized_tiles[pos[1]][pos[0]] = "#"

    # Get the current item
    cur = tiles[pos[1]][pos[0]]

    if cur == '.':
        if direction == 'r':
            next_pos = (pos[0] + 1, pos[1])
        elif direction == 'l':
            next_pos = (pos[0] - 1, pos[1])
        elif direction == 'd':
            next_pos = (pos[0], pos[1] + 1)
        elif direction == 'u':
            next_pos = (pos[0], pos[1] - 1)

        add_next(next_pos, direction)

    elif cur == '/':
        # Reflect
        if direction == 'r':
             # Reflect up
            next_direction = 'u'
            next_pos = (pos[0], pos[1] - 1)
        elif direction == 'l':
            # Reflect down
            next_direction = 'd'
            next_pos = (pos[0], pos[1] + 1)
        elif direction == 'd':
            # Reflect left
            next_direction = 'l'
            next_pos = (pos[0] - 1, pos[1])
        elif direction == 'u':
            # Reflect right
            next_direction = 'r'
            next_pos = (pos[0] + 1, pos[1])

        add_next(next_pos, next_direction)

    elif cur == '\\':
        # Reflect
        if direction == 'r':
             # Reflect down
            next_direction = 'd'
            next_pos = (pos[0], pos[1] + 1)
        elif direction == 'l':
            # Reflect up
            next_direction = 'u'
            next_pos = (pos[0], pos[1] - 1)
        elif direction == 'd':
            # Reflect right
            next_direction = 'r'
            next_pos = (pos[0] + 1, pos[1])
        elif direction == 'u':
            # Reflect left
            next_direction = 'l'
            next_pos = (pos[0] - 1, pos[1])

        add_next(next_pos, next_direction)

    elif cur == '-':
        if direction == 'r':
            next_pos = (pos[0] + 1, pos[1])
            add_next(next_pos, direction)
        elif direction == 'l':
            next_pos = (pos[0] - 1, pos[1])
            add_next(next_pos, direction)
        elif direction == 'u' or direction == 'd':
            l_pos = (pos[0] - 1, pos[1])
            add_next(l_pos, 'l')

            r_pos = (pos[0] + 1, pos[1])
            add_next(r_pos, 'r')

    elif cur == '|':
        if direction == 'd':
            next_pos = (pos[0], pos[1] + 1)
            add_next(next_pos, direction)
        elif direction == 'u':
            next_pos = (pos[0], pos[1] - 1)
            add_next(next_pos, direction)
        elif direction == 'r' or direction == 'l':
            d_pos = (pos[0], pos[1] + 1)
            add_next(d_pos, 'd')

            u_pos = (pos[0], pos[1] - 1)
            add_next(u_pos, 'u')




max_energized = 0
max_energized_tiles = []


for j in range(0, len(tiles)):
    energized_tiles = []
    for line in tiles:
        cur = []
        for _ in line:
            cur.append(".")
        energized_tiles.append(cur)
    direction_cache = set()

    next_tiles = [{"pos": (0, j), "dir": 'r'}]

    while len(next_tiles) > 0:
        energize_tiles(next_tiles[0]["pos"], next_tiles[0]["dir"])
        next_tiles = next_tiles[1:]

    total = 0
    for line in energized_tiles:
        for c in line:
            if c == "#":
                total += 1

    if total > max_energized:
        max_energized = total
        max_energized_tiles = energized_tiles

for i in range(0, len(tiles[0])):
    energized_tiles = []
    for line in tiles:
        cur = []
        for _ in line:
            cur.append(".")
        energized_tiles.append(cur)
    direction_cache = set()
    next_tiles = [{"pos": (i, 0), "dir": 'd'}]

    while len(next_tiles) > 0:
        energize_tiles(next_tiles[0]["pos"], next_tiles[0]["dir"])
        next_tiles = next_tiles[1:]

    total = 0
    for line in energized_tiles:
        for c in line:
            if c == "#":
                total += 1
    print(total)

    if total > max_energized:
        max_energized = total
        max_energized_tiles = energized_tiles


for j in range(0, len(tiles)):
    energized_tiles = []
    for line in tiles:
        cur = []
        for _ in line:
            cur.append(".")
        energized_tiles.append(cur)
    direction_cache = set()
    next_tiles = [{"pos": (len(tiles[0]) - 1, j), "dir": 'l'}]

    while len(next_tiles) > 0:
        energize_tiles(next_tiles[0]["pos"], next_tiles[0]["dir"])
        next_tiles = next_tiles[1:]

    total = 0
    for line in energized_tiles:
        for c in line:
            if c == "#":
                total += 1
    print(total)
    if total == 0:
        print(tiles[j][len(tiles[0]) - 1])

    if total > max_energized:
        max_energized = total
        max_energized_tiles = energized_tiles

for i in range(0, len(tiles[0])):
    energized_tiles = []
    for line in tiles:
        cur = []
        for _ in line:
            cur.append(".")
        energized_tiles.append(cur)
    direction_cache = set()
    next_tiles = [{"pos": (i, len(tiles) - 1), "dir": 'u'}]

    while len(next_tiles) > 0:
        energize_tiles(next_tiles[0]["pos"], next_tiles[0]["dir"])
        next_tiles = next_tiles[1:]

    total = 0
    for line in energized_tiles:
        for c in line:
            if c == "#":
                total += 1
    print(total)

    if total > max_energized:
        max_energized = total
        max_energized_tiles = energized_tiles

print(max_energized)
for line in max_energized_tiles:
    print("".join(line))
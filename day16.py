#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

tiles = [line.strip() for line in lines]

energized_tiles = []
for line in tiles:
    cur = []
    for _ in line:
        cur.append(".")
    energized_tiles.append(cur)

direction_cache = set()

# Energize the tile at (x, y), given a certain direction in 'u', 'd', 'l', 'r'
# Then figure out what the next direction to go in is.
def energize_tiles(pos, direction):
    # Check x is within bounds
    if pos[0] < 0 or pos[0] > len(tiles[0]):
        return

    # Check y is within bounds
    if pos[1] < 0 or pos[1] > len(tiles):
        return

    # Only go in a certain direction, from a starting point, once
    if (start_pos, direction) in direction_cache:
        return
    direction_cache.add(start_pos, direction)

    # Energize the current pos
    energized_tiles[start_pos[pos[1]]][pos[0]] = "#"

    # Get the current item
    cur = tiles[pos[1]][pos[0]]

    if cur == ".":
        if direction == 'r':
            next_pos = (pos[0] + 1, pos[1])


        energize_tiles(next_pos, direction)

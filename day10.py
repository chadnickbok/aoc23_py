#!/usr/bin/env python3

import sys

east = 0
west = 1
north = 2
south = 3

pipe_dirs = {
    "|": set([north, south]),
    "-": set([east, west]),
    "L": set([north, east]),
    "J": set([north, west]),
    "7": set([south, west]),
    "F": set([south, east]),
    ".": set(),
}


def next_dir(pipe, in_dir):
    dirs = pipe_dirs[pipe]
    if not in_dir in dirs:
        print(pipe, "in_dir not in dirs")
        return None

    #XXX: How to get the "other" value from a set?
    next_dir = None
    for d in dirs:
        if d is not in_dir:
            next_dir = d
            break

    return next_dir

with open(sys.argv[1]) as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

for y in range(0, len(lines)):
    for x in range(0, len(lines[0])):
        if lines[y][x] == "S":
            start = (x, y)

print("start:", start)

up = lines[start[1] - 1][start[0]]
down = lines[start[1] + 1][start[0]]
left = lines[start[1]][start[0] - 1]
right = lines[start[1]][start[0] + 1]

print("up", up, next_dir(up, south))
print("down", down, next_dir(down, north))
print("left", left, next_dir(left, west))
print("right", right, next_dir(right, east))

if next_dir(up, south) is not None:
    cur_pos = (start[0], start[1] - 1)
    from_dir = south
elif next_dir(down, north) is not None:
    cur_pos = (start[0], start[1] + 1)
    from_dir = north
elif next_dir(right, west) is not None:
    cur_pos = (start[0] + 1, start[1])
    from_dir = west
elif next_dir(left, east) is not None:
    cur_pos = (start[0] - 1, start[1])
    from_dir = east


pipe_positions = set([start, cur_pos])
print("starting at", cur_pos)
count = 0
while cur_pos != start:
    cur_pipe = lines[cur_pos[1]][cur_pos[0]]
    d = next_dir(cur_pipe, from_dir)

    if d == north:
        cur_pos = (cur_pos[0], cur_pos[1] - 1)
        from_dir = south
    elif d == south:
        cur_pos = (cur_pos[0], cur_pos[1] + 1)
        from_dir = north
    elif d == east:
        cur_pos = (cur_pos[0] + 1, cur_pos[1])
        from_dir = west
    elif d == west:
        cur_pos = (cur_pos[0] - 1, cur_pos[1])
        from_dir = east
    else:
        break
    
    count += 1
    pipe_positions.add(cur_pos)

print(count // 2 + 1)

print("Finding enclosed squares")

lines[start[1]] = lines[start[1]].replace('S', 'J')

enclosed_count = 0
for j in range(0, len(lines)):
    for i in range(0, len(lines[0])):
        cur_pos = (i, j)
        if cur_pos in pipe_positions:
            continue

        up_count = 0
        down_count = 0

        for x in range(i + 1, len(lines[0])):
            if (x, j) in pipe_positions:
                p = lines[j][x]
                if p == "-" or p == ".":
                    continue
                if p == "|":
                    up_count += 1
                    down_count += 1
                elif p in ['J', 'L']:
                    up_count += 1
                else:
                    down_count += 1

        if up_count > 0 and down_count > 0:
            pipes = min(up_count, down_count)
            if pipes % 2 == 1:
                enclosed_count += 1

print(enclosed_count)


#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()


digs = []
for line in lines:
    parts = line.strip().split()
    digs.append((parts[0], int(parts[1]), parts[2]))

vertical = 0
horizontal = 0
for dig in digs:
    print(dig)

    if dig[0] in ['R', 'L']:
        horizontal += dig[1]
    else:
        vertical += dig[1]
print(horizontal, vertical)

ground = []
for j in range(0, vertical * 2):
    cur = []
    for i in range(0, horizontal * 2):
        cur.append(".")
    ground.append(cur)


cur_pos = (horizontal, vertical)

for dig in digs:
    next_x, next_y = cur_pos[0], cur_pos[1]

    start_x, end_x, start_y, end_y = cur_pos[0], cur_pos[0], cur_pos[1], cur_pos[1]

    if dig[0] == 'U':
        next_y = start_y - dig[1]
        start_y = next_y
        end_x += 1
    elif dig[0] == 'D':
        next_y = start_y + dig[1]
        end_y = next_y
        end_x += 1
    elif dig[0] == 'L':
        next_x = start_x - dig[1]
        start_x = next_x
        end_x += 1
        end_y += 1
    elif dig[0] == 'R':
        next_x = end_x + dig[1] 
        end_x = next_x
        end_y += 1

    print(start_x, end_x, start_y, end_y)

    for j in range(start_y, end_y):
        for i in range(start_x, end_x):
            ground[j][i] = "#"

    cur_pos = (next_x, next_y)

for g in ground:
    print("".join(g))


empty_q = [(0, 0)]
visited = set()

while len(empty_q) > 0:
    cur = empty_q.pop()

    if cur[0] < 0 or cur[0] >= (horizontal * 2):
        continue

    if cur[1] < 0 or cur[1] >= (vertical * 2):
        continue

    if ground[cur[1]][cur[0]] == "#":
        continue

    if cur in visited:
        continue
    visited.add(cur)

    empty_q.append((cur[0] - 1, cur[1]))
    empty_q.append((cur[0] + 1, cur[1]))
    empty_q.append((cur[0], cur[1] - 1))
    empty_q.append((cur[0], cur[1] + 1))

print(len(visited))

print(vertical * 2 * horizontal * 2 - len(visited))
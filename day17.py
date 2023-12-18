#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

heats = []
for line in lines:
    cur = []
    for c in line.strip():
        cur.append(int(c))
    heats.append(cur)


def insert_sorted(q, node):
    i = 0
    for i, n in enumerate(q):
        if node["cost"] < n["cost"]:
            q.insert(i, node)
            return
    q.append(node)


# find the path that minimizes the heat lost
def findMinHeat(startPos, endPos):

    posQ = [{
        # Pos, Dir, Cost - Tuple for hashing
        "node": (startPos, 'o', 0),
        "cost": 0,
        "path": []
    }]

    visited = set()

    while len(posQ) > 0:
        cur = posQ.pop(0)

        # Only visit each node once
        if cur["node"] in visited:
            continue

        visited.add(cur["node"])

        cur_pos = cur["node"][0]
        cur_dir = cur["node"][1]
        cur_count = cur["node"][2]

        if cur_pos == endPos and cur_count > 3:
            print("Final cost", cur)
            return cur["cost"]

        # Go right
        r_pos = (cur_pos[0] + 1, cur_pos[1])
        if cur_dir != "l" and r_pos[0] < len(heats[0]):
            r_count = 1
            if cur_dir == "r" or cur_dir =="o":
                r_count = cur_count + 1

            if (cur_dir in ["r", "o"] and r_count < 11) or (cur_dir != "r" and cur_count > 3):
                insert_sorted(posQ, {
                    "node": (r_pos, 'r', r_count),
                    "cost": cur["cost"] + heats[r_pos[1]][r_pos[0]],
                    "path": cur["path"] + ["r"]
                })

        # Go left
        l_pos = (cur_pos[0] - 1, cur_pos[1])
        if cur_dir != "r" and l_pos[0] > 0:
            l_count = 1
            if cur["node"][1] == "l":
                l_count = cur_count + 1

            if (cur_dir == "l" and l_count < 11) or (cur_dir != "l" and cur_count > 3):
                insert_sorted(posQ, {
                    "node": (l_pos, 'l', l_count),
                    "cost": cur["cost"] + heats[l_pos[1]][l_pos[0]],
                    "path": cur["path"] + ["l"]
                })

        # Go down
        d_pos = (cur_pos[0], cur_pos[1] + 1)
        if cur_dir != "u" and d_pos[1] < len(heats):
            d_count = 1
            if cur["node"][1] in ["d", "o"]:
                d_count = cur["node"][2] + 1

            if (cur_dir in ["d", "o"] and d_count < 11) or (cur_dir != "d" and cur_count > 3):
                insert_sorted(posQ, {
                    "node": (d_pos, 'd', d_count),
                    "cost": cur["cost"] + heats[d_pos[1]][d_pos[0]],
                    "path": cur["path"] + ["d"]
                })

        # Go up
        u_pos = (cur_pos[0], cur_pos[1] - 1)
        if cur_dir != "d" and u_pos[1] > 0:
            u_count = 1
            if cur["node"][1] == "u":
                u_count = cur["node"][2] + 1

            if (cur_dir == "u" and u_count < 11) or (cur_dir != "u" and cur_count > 3):
                insert_sorted(posQ, {
                    "node": (u_pos, 'u', u_count),
                    "cost": cur["cost"] + heats[u_pos[1]][u_pos[0]],
                    "path": cur["path"] + ["u"]
                })


print((len(heats[0]), len(heats)))
findMinHeat((0, 0), (len(heats[0]) - 1, len(heats) - 1))
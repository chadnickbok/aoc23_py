#!/usr/bin/env python3

import sys
import math

class Node():
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.name} = ({self.left}, {self.right})"

with open(sys.argv[1]) as f:
    lines = f.readlines()

commands = lines[0].strip()


nodes = {}
for line in lines[2:]:
    parts = line.strip().split("=")
    name = parts[0].strip()
    parts = parts[1].strip().split(",")
    left = parts[0][1:]
    right = parts[1][1:-1]
    nodes[name] = Node(name, left, right)


#start = nodes["AAA"]
#print(start.name, start.left, start.right)

#cur = start
#steps = 0
#while cur.name != "ZZZ":
#    c = commands[steps % len(commands)]
#    if c == "L":
#        cur = nodes[cur.left]
#    else:
#        cur = nodes[cur.right]
#
#    steps += 1

#print(steps)

starts = []
for node_name in nodes:
    if node_name.endswith("A"):
        starts.append(nodes[node_name])

ends = []
for cur in starts:
    steps = 0
    
    while not cur.name.endswith("Z"):
        c = commands[steps % len(commands)]
        if c == "L":
            cur = nodes[cur.left]
        else:
            cur = nodes[cur.right]
        steps += 1

    print(steps)
    ends.append(steps)

print(math.lcm(*ends))

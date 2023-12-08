#!/usr/bin/env python3

import sys

class Node():
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right


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


start = nodes["AAA"]
print(start.name, start.left, start.right)

cur = start
steps = 0
while cur.name != "ZZZ":
    c = commands[steps % len(commands)]
    if c == "L":
        cur = nodes[cur.left]
    else:
        cur = nodes[cur.right]

    steps += 1

print(steps)


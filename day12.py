#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()


for line in lines:
    parts = line.strip().split()
    springs = parts[0]
    runs = [int(x) for x in parts[1].split(",")]


    print(springs, runs)

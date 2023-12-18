#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

for line in lines:
    print(line)

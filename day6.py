#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

times = [int(x) for x in lines[0].split(":")[1].strip().split()]
distances = [int(x) for x in lines[1].split(":")[1].strip().split()]

results = 1
for i in range(0, len(times)):
    wins = 0
    for speed in range(0, times[i]):
        distance = speed * (times[i] - speed)
        
        if distance > distances[i]:
            wins += 1
    results = results * wins

print(results)

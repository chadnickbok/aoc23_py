#!/usr/bin/env python3

import re

with open("day1.txt") as f:
    lines = f.readlines()

def get_calibration(line):
    matches = re.findall("\d", line)
    print(matches)
    return 10 * int(matches[0]) + int(matches[-1])

calibrations = []
for line in lines:
    calibration = get_calibration(line)
    print(calibration)
    calibrations.append(calibration)

print(sum(calibrations))

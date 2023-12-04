#!/usr/bin/env python3

import re

with open("day1.txt") as f:
    lines = f.readlines()

vals = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

def get_calibration(line):
    matches = []
    for i in range(0, len(line)):
        m = re.match("\d|one|two|three|four|five|six|seven|eight|nine", line[i:])
        if m:
            matches.append(vals[m[0]])
    print(line, matches)
    return 10 * int(matches[0]) + int(matches[-1])

calibrations = []
for line in lines:
    calibration = get_calibration(line)
    print(calibration)
    calibrations.append(calibration)

print(sum(calibrations))

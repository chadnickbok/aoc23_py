#!/usr/bin/env python3

import sys
import json

with open(sys.argv[1]) as f:
    lines = f.readlines()


inputs = lines[0].strip().split(",")

boxes = {}
for i in range(0, 256):
    boxes[i] = []

for i in inputs:

    i = i.encode('utf-8')
    cur = 0

    for c in i:
        if c in b'-=':
            break
        cur += c
        cur = cur * 17
        cur = cur % 256

    print("c", c, "=", b"=")
    if c in b'=':
        parts = i.split(b"=")
        label = str(parts[0])
        focal_len = int(parts[1])

        found = False
        for lens in boxes[cur]:
            if lens["label"] == label:
                lens["focal_len"] = focal_len
                found = True
                break

        if not found:
            boxes[cur].append({
                "label": label,
                "focal_len": focal_len,
            })

    else:
        label = str(i.split(b"-")[0])
        location = -1
        for i, lens in enumerate(boxes[cur]):
            if lens["label"] == label:
                location = i
                break
        if location >= 0:
            del(boxes[cur][location])

    #print(json.dumps(boxes, indent=2))


total = 0
for i in range(0, 256):
    for j in range(0, len(boxes[i])):
        power = (i + 1) * (j + 1) * boxes[i][j]["focal_len"]
        total += power
        print(boxes[i][j]["label"], power)
print(total)

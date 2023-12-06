#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

seeds = [int(x) for x in lines[0].strip().split(":")[1].strip().split()]
print(seeds)

seed_count = 0
for i in range(0, len(seeds) // 2):
    seed_count += seeds[i * 2 + 1]
print("Seed count:", seed_count)


class RangeMap():
    def __init__(self, dest_start, source_start, range_len): 
        self.dest_start = dest_start
        self.source_start = source_start
        self.range_len = range_len

    def contains_value(self, val):
        if val >= self.source_start and val < self.source_start + self.range_len:
            return True
        return False

    def map_value(self, val):
        offset = val - self.source_start
        return offset + self.dest_start


class RangeMapper():
    def __init__(self):
        self.ranges = []

    def add_range(self, dest_start, source_start, range_len):
        self.ranges.append(RangeMap(dest_start, source_start, range_len))

    def map_value(self, val):
        for r in self.ranges:
            if r.contains_value(val):
                return r.map_value(val)
        return val


seed_to_soil = RangeMapper()
soil_to_fertilizer = RangeMapper()
fertilizer_to_water = RangeMapper()
water_to_light = RangeMapper()
light_to_temperature = RangeMapper()
temperature_to_humidity = RangeMapper()
humidity_to_location = RangeMapper()

cur_map = seed_to_soil
for line in lines[1:]:
    line = line.strip()
    if len(line) == 0:
        continue

    if line.startswith("seed-to"):
        cur_map = seed_to_soil
        continue

    if line.startswith("soil-to"):
        cur_map = soil_to_fertilizer
        continue

    if line.startswith("fertilizer-to"):
        cur_map = fertilizer_to_water
        continue

    if line.startswith("water-to"):
        cur_map = water_to_light
        continue

    if line.startswith("light-to"):
        cur_map = light_to_temperature
        continue

    if line.startswith("temperature-to"):
        cur_map = temperature_to_humidity
        continue

    if line.startswith("humidity-to"):
        cur_map = humidity_to_location
        continue

    parts = [int(x) for x in line.split()]

    dest_start = parts[0]
    source_start = parts[1]
    range_len = parts[2]
    
    cur_map.add_range(dest_start, source_start, range_len)


def map_seed_to_location(seed):
    soil = seed_to_soil.map_value(seed)
    fertilizer = soil_to_fertilizer.map_value(soil)
    water = fertilizer_to_water.map_value(fertilizer)
    light = water_to_light.map_value(water)
    temperature = light_to_temperature.map_value(light)
    humidity = temperature_to_humidity.map_value(temperature)
    location = humidity_to_location.map_value(humidity)

    #print(soil, fertilizer, water, light, temperature, humidity, location)

    return location

min_location = map_seed_to_location(seeds[0])

count = 0
for i in range(0, len(seeds) // 2):
    for offset in range(0, seeds[i * 2 + 1]):
        count += 1
        if count % 1000000 == 0:
            print(count)
        seed = seeds[i * 2] + offset
        cur = map_seed_to_location(seed)
        if cur < min_location:
            min_location = cur
            print(seed, cur)

print(min_location)

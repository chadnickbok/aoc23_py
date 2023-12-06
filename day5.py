#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

seeds = [int(x) for x in lines[0].strip().split(":")[1].strip().split()]
print(seeds)

seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}


cur_map = seed_to_soil
for line in lines[1:]:
    print(line)
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

    for i in range(0, range_len):
        cur_map[source_start + i] = dest_start + i


def map_seed_to_location(seed):
    soil = seed
    if seed in seed_to_soil:
        soil = seed_to_soil[seed]

    fertilizer = soil
    if soil in soil_to_fertilizer:
        fertilizer = soil_to_fertilizer[soil]

    water = fertilizer
    if fertilizer in fertilizer_to_water:
        water = fertilizer_to_water[fertilizer]

    light = water
    if water in water_to_light:
        light = water_to_light[water]

    temperature = light
    if light in light_to_temperature:
        temperature = light_to_temperature[light]

    humidity = temperature
    if temperature in temperature_to_humidity:
        humidity = temperature_to_humidity[temperature]

    location = humidity
    if humidity in humidity_to_location:
        location = humidity_to_location[humidity]

    return location

locations = []
for seed in seeds:
    locations.append(map_seed_to_location(seed))

print(min(locations))

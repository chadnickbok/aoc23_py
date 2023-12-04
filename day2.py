#!/usr/bin/env python3

max_red = 12
max_green = 13
max_blue = 14

max_vals = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_subset_max(max_vals, subset):
    cubes = subset.split(",")
    for cube in cubes:
        parts = cube.strip().split(" ")
        count = int(parts[0])
        color = parts[1]

        if max_vals[color] < count:
            max_vals[color] = count


def game_power(game):
    max_vals = {"red": 0, "green": 0, "blue": 0}

    subsets = game.split(";")
    for subset in subsets:
        get_subset_max(max_vals, subset)

    return max_vals["red"] * max_vals["green"] * max_vals["blue"]


with open("day2.txt") as f:
    lines = f.readlines()

game_results = []
for line in lines:
    parts = line.strip().split(":")
    game_num = int(parts[0].split()[1])
    game_results.append(game_power(parts[1]))

print(game_results)
print(sum(game_results))

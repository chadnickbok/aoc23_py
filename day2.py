#!/usr/bin/env python3

max_red = 12
max_green = 13
max_blue = 14

max_vals = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def is_possible_subset(subset):
    cubes = subset.split(",")
    for cube in cubes:
        parts = cube.strip().split(" ")
        count = int(parts[0])
        color = parts[1]

        if max_vals[color] < count:
            return False

    return True


def is_possible(game):
    subsets = game.split(";")
    for subset in subsets:
        if not is_possible_subset(subset):
            return False
    return True


with open("day2.txt") as f:
    lines = f.readlines()

possible_games = []
for line in lines:
    parts = line.strip().split(":")
    game_num = int(parts[0].split()[1])

    if is_possible(parts[1]):
        possible_games.append(game_num)

print(possible_games)
print(sum(possible_games))

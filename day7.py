#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

card_vals = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

class Hand():
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        
        counts = {}
        for c in cards:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        self.hand_type = 0
        if len(counts) == 5:
            # High Card
            self.hand_type = 1
        elif len(counts) == 4:
            # One Pair
            self.hand_type = 2
        elif len(counts) == 3:
            if max(counts.values()) == 2:
                # Two pair
                self.hand_type = 3
            else:
                # Three of a kind
                self.hand_type = 4
        elif len(counts) == 2:
            if max(counts.values()) == 3:
                # Full house
                self.hand_type = 5
            else:
                # Four of a kind
                self.hand_type = 6
        else:
            self.hand_type = 7

    def __lt__(self, other):
        if self.hand_type == other.hand_type:
            for i, c in enumerate(self.cards):
                if c == other.cards[i]:
                    continue
                l = card_vals[c]
                r = card_vals[other.cards[i]]
                return l < r

        return self.hand_type < other.hand_type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.cards + " " + str(self.hand_type) + " " + str(self.bid)

hands = []
for line in lines:
    parts = line.strip().split()
    hands.append(Hand(parts[0], int(parts[1])))

print(hands)
hands.sort()
print(hands)

result = 0
for i, hand in enumerate(hands):
    result += (i + 1) * hand.bid
print(result)

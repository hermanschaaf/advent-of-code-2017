#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict, namedtuple
Position = namedtuple("Position", "x y")

# r, c
dirs = [
    Position(0, 1),  # E
    Position(-1, 0),  # N
    Position(0, -1),  # W
    Position(1, 0),  # S
]

alldirs = [
    Position(0, 1),  # E
    Position(-1, 0),  # N
    Position(0, -1),  # W
    Position(1, 0),  # S
    Position(1, 1),
    Position(-1, -1),
    Position(1, -1),
    Position(-1, 1),
]


class Dir(object):

    def __init__(self):
        self.dirs = dirs
        self.curr = 0

    def next(self):
        return self.dirs[(self.curr + 1) % len(self.dirs)]

    def turn(self):
        self.curr = (self.curr + 1) % len(self.dirs)
        return self.get()

    def get(self):
        return self.dirs[self.curr]


if __name__ == "__main__":
    q = int(input())
    size = 1001
    ar = [[0 for c in range(size)] for r in range(size)]
    org = Position(size//2, size//2)
    ar[org.x][org.y] = 1
    d = Dir()
    pos = [org.x, org.y]
    while True:
        pos[0] += d.get().x
        pos[1] += d.get().y
        v = sum(ar[pos[0] + x][pos[1] + y] for x, y in alldirs)
        ar[pos[0]][pos[1]] = v
        nx, ny = d.next()
        if ar[pos[0] + nx][pos[1] + ny] == 0:
            d.turn()

        if v > q:
            break
    for row in ar:
        print(row)
    print(v)

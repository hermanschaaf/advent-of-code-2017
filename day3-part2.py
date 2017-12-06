#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict, namedtuple


class Pos(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({},{})".format(self.x, self.y)

dirs = [Pos(1, 0), Pos(0, -1), Pos(-1, 0), Pos(0, 1)]
alldirs = [Pos(x, y) for x in range(-1, 2) for y in range(-1, 2) if x | y != 0]


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
    org = Pos(size//2, size//2)
    ar[org.x][org.y] = 1
    d = Dir()
    pos = Pos(org.x, org.y)
    while True:
        pos.x += d.get().x
        pos.y += d.get().y
        v = sum(ar[pos.x + add.x][pos.y + add.y] for add in alldirs)
        ar[pos.x][pos.y] = v
        nxt = d.next()
        if ar[pos.x + nxt.x][pos.y + nxt.y] == 0:
            d.turn()

        if v > q:
            break

    print(v)

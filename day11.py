#!/bin/python

from __future__ import print_function, unicode_literals

import math
import sys

from collections import defaultdict, namedtuple

sys.setrecursionlimit(10000)

Pos = namedtuple("Pos", "x y")

dirs = {
    'n': Pos(0, -1),
    's': Pos(0, 1),
    'ne': Pos(0.5, -0.5),
    'nw': Pos(-0.5, -0.5),
    'se': Pos(0.5, 0.5),
    'sw': Pos(-0.5, 0.5),
}


def shortest(p):
    h = abs(p.x // 0.5)
    v = max(0, abs(p.y) - h * 0.5)
    return round(h + v)


def solve_part1(s):
    D = s.strip().split(',')
    x = [0, 0]
    for d in D:
        pos = dirs[d]
        x[0] += pos[0]
        x[1] += pos[1]

    steps = shortest(Pos(x[0], x[1]))
    return steps


def test_part1():
    TestCase = namedtuple("TestCase", "give want")
    cases = [
        TestCase("ne,ne,ne", 3),
        TestCase("ne,ne,sw,sw", 0),
        TestCase("ne,ne,s,s", 2),
        TestCase("se,sw,se,sw,sw", 3),
    ]
    for cs in cases:
        got = solve_part1(cs.give)
        assert got == cs.want, "{} = {}, want {}".format(cs.give, got, cs.want)


def solve_part2(s):
    D = s.strip().split(',')
    x = [0, 0]
    mx = 0
    for d in D:
        pos = dirs[d]
        x[0] += pos[0]
        x[1] += pos[1]
        mx = max(mx, shortest(Pos(x[0], x[1])))
    return mx


if __name__ == "__main__":
    test_part1()
    s = input()
    print(solve_part1(s))
    print(solve_part2(s))

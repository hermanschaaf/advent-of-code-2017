#!/bin/python

from __future__ import print_function, unicode_literals

import re

from collections import defaultdict


def clean(s):
    ignore = False
    garbage = False
    c = []
    cnt = 0
    for ch in s:
        if ignore:
            ignore = False
            continue

        if ch == "<" and not garbage:
            garbage = True
            continue
        elif ch == "!":
            ignore = True
            continue

        if garbage and ch == ">":
            garbage = False
        elif not garbage:
            c.append(ch)
        else:
            cnt += 1
    return "".join(c), cnt


def count(s):
    s, garbage_cnt = clean(s)
    # print(s)
    cnt, d = 0, 1
    for ch in s:
        if ch == "{":
            cnt += d
            d += 1
        elif ch == "}":
            d -= 1
    return cnt, garbage_cnt


def test():
    cases = [["{}", 1],
             ["{{{}}}", 6],
             ["{{},{}}", 5],
             ["{{{},{},{{}}}}", 16],
             ["{<a>,<a>,<a>,<a>}", 1],
             ["{{<ab>},{<ab>},{<ab>},{<ab>}}", 9],
             ["{{<!!>},{<!!>},{<!!>},{<!!>}}", 9],
             ["{{<a!>},{<a!>},{<a!>},{<ab>}}", 3],
             ["{{<!>},{<!>},{<!>},{<a>}}", 3],
             ["{{<a>},{<a>},{<a>},{<a>}}", 9],
             ["{<a>,<a>,<a>,<a>}", 1],
             ["{<{},{},{{}}>}", 1],
             ["{<!!!>>}", 1],
             ]
    for give, want in cases:
        assert count(give)[0] == want

if __name__ == "__main__":
    q = input().strip()
    test()
    a, b = count(q)
    print(a, b)

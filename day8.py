#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict


def condition(a, comp, b, d):
    if comp == "==":
        return d[a] == int(b)
    if comp == "!=":
        return d[a] != int(b)
    if comp == "<=":
        return d[a] <= int(b)
    if comp == ">=":
        return d[a] >= int(b)
    if comp == "<":
        return d[a] < int(b)
    if comp == ">":
        return d[a] > int(b)
    raise Exception("condition not found " + comp)

if __name__ == "__main__":
    d = defaultdict(int)
    mx = 0
    while True:
        try:
            line = input().strip().split(" ")
        except:
            break
        var, cmd, val, _, a, comp, b = line
        val = -1 * int(val) if cmd == "dec" else int(val)
        if condition(a, comp, b, d):
            d[var] += val
            mx = max(mx, d[var])
    print(max(v for v in d.values()))
    print(mx)

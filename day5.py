#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict


def solve(vals):
    i = 0
    n = len(vals)
    steps = 0
    while i < n:
        tmp = i
        i += vals[i]
        if vals[tmp] >= 3:
            vals[tmp] -= 1
        else:
            vals[tmp] += 1
        steps += 1
    return steps

if __name__ == "__main__":
    vals = []
    while True:
        try:
            q = int(input())
        except:
            break
        vals.append(q)
    print(solve(vals))

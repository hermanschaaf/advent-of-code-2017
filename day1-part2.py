#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict


def special_sum(n):
    d = str(n)
    l = len(d)
    s = 0
    for i in range(l):
        a, b = d[i], d[(i+l//2) % l]
        if a == b:
            s += int(a)
    return s


if __name__ == "__main__":
    q = int(input())
    print(special_sum(q))

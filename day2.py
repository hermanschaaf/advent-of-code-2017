#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict

if __name__ == "__main__":
    s = 0
    while True:
        try:
            row = list(map(int, filter(None, input().strip().split(" "))))
        except Exception as e:
            break
        mx, mn = max(row), min(row)
        s += mx - mn
    print(s)

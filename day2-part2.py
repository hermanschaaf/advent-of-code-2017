#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict


def evendiv(row):
    n = len(row)
    for i in range(n):
        for u in range(i+1, n):
            a, b = row[i], row[u]
            if b > a:
                a, b = b, a

            if a % b == 0:
                # print(a, b)
                return a // b

if __name__ == "__main__":
    s = 0
    while True:
        try:
            row = list(map(int, filter(None, input().strip().split(" "))))
        except Exception as e:
            break
        s += evendiv(row)
    print(s)

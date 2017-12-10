#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict

if __name__ == "__main__":
    lens = list(map(int, input().strip().split(",")))
    n = 256
    A = [i for i in range(n)]
    pos = 0
    skip = 0
    for ln in lens:
        a, b = pos, pos + ln - 1
        for i in range(ln // 2):
            A[a % n], A[b % n] = A[b % n], A[a % n]
            a += 1
            b -= 1
        pos += ln + skip
        skip += 1
        print(A, pos, skip)
    print(A)
    print(A[0] * A[1])

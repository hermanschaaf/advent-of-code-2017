#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict


def xor(nums):
    n = 0
    for nm in nums:
        n ^= nm
    return n

if __name__ == "__main__":
    lens = list(map(ord, input().strip()))
    lens += [17, 31, 73, 47, 23]
    n = 256
    A = [i for i in range(n)]
    pos = 0
    skip = 0
    for r in range(64):
        for ln in lens:
            a, b = pos, pos + ln - 1
            for i in range(ln // 2):
                A[a % n], A[b % n] = A[b % n], A[a % n]
                a += 1
                b -= 1
            pos += ln + skip
            skip += 1
        # print(A, pos, skip)

    # get sparse hash
    s = []
    for b in range(0, n, 16):
        s.append(xor(A[b:b+16]))
    for h in s:
        print("{0:02x}".format(h), end="")
    print()

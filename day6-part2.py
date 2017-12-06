#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict


def seen(A, hist):
    if A in hist:
        return True
    hist.append(A[:])


def distribute(A):
    n = len(A)
    i = A.index(max(A))
    val, A[i] = A[i], 0
    for u in range(1, val+1):
        A[(i + u) % n] += 1


def solve(A):
    hist = []
    cnt = 0
    while True:
        # print(A)
        if seen(A, hist):
            return len(hist) - hist.index(A)
        distribute(A)
        cnt += 1

if __name__ == "__main__":
    A = list(map(int, input().strip().split("\t")))
    print(solve(A))

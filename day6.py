#!/bin/python

from __future__ import print_function, unicode_literals


def seen(A, hist):
    if str(A) in hist:
        return True
    hist[str(A)] = len(hist)


def distribute(A):
    n = len(A)
    i = A.index(max(A))
    val, A[i] = A[i], 0
    for u in range(1, val+1):
        A[(i + u) % n] += 1


def solve(A, part):
    hist = {}
    cnt = 0
    while True:
        # print(A)
        if seen(A, hist):
            if part == 1:
                return cnt
            elif part == 2:
                return cnt - hist[str(A)]
        distribute(A)
        cnt += 1

if __name__ == "__main__":
    A = list(map(int, input().strip().split("\t")))
    print(solve(A, 1))
    print(solve(A, 2))

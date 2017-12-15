#!/bin/python

from __future__ import print_function, unicode_literals


A = 277
B = 349

# A = 65
# B = 8921
d = 2147483647


def nextA(start):
    A = start
    while True:
        A = (A * 16807) % d
        yield A


def nextB(start):
    B = start
    while True:
        B = (B * 48271) % d
        yield B

genA = nextA(A)
genB = nextB(B)
cnt = 0
mask = (1 << 16) - 1
for i in range(40000000):
    a, b = next(genA), next(genB)
    if a & mask == b & mask:
        cnt += 1

print(cnt)

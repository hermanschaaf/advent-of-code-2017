#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict


def special_sum(i):
    n = i
    while n > 0:
        f = n % 10
        n //= 10

    s = 0
    n = f
    while i > 0:
        c = i % 10
        i //= 10
        if c == n:
            s += c
        n = c
    return s


if __name__ == "__main__":
    q = int(input())
    print(special_sum(q))

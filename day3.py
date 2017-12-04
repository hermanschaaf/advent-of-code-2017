#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict

if __name__ == "__main__":
    upto = int(input())
    c = 1
    while c ** 2 < upto:
        c += 2
    print(upto, c**2)
    print("between", ((c-1) // 2), c-1)
    se = c**2
    sw = se - (c - 1)
    nw = sw - (c - 1)
    ne = nw - (c - 1)

    print(se, sw, nw, ne)
    print(c-1 - (ne - upto))

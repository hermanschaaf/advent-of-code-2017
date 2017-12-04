#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict

if __name__ == "__main__":
    t = 0
    while True:
        try:
            s = input().strip().split(" ")
        except:
            break
        t += 1 if len(set(s)) == len(s) else 0
    print(t)

#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict


def isvalid(s):
    sets = []
    for word in s:
        st = set(word)
        if any(st == st2 for st2 in sets):
            return False
        sets.append(st)
    return True

if __name__ == "__main__":
    t = 0
    while True:
        try:
            s = input().strip().split(" ")
        except:
            break
        t += 1 if isvalid(s) else 0
    print(t)

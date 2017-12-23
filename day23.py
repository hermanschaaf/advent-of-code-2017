from __future__ import print_function

import sys

from collections import defaultdict, deque


class D(defaultdict):

    def __getitem__(self, k):
        try:
            v = int(k)
            return v
        except:
            return super(D, self).__getitem__(k)


class Program(object):

    def __init__(self, lines, p):
        self.lines = lines
        self.d = D(int)
        self.d['a'] = 1
        self.i = 0
        self.q = deque([])
        self.progressed = True
        self.mul_calls = 0

    def next(self):
        if self.i < 0 or self.i >= len(self.lines):
            self.progressed = False
            return

        d = self.d

        parts = lines[self.i].strip().split(" ")
        cmd = parts[0]
        c, v = parts[1:]
        if cmd == "set":
            d[c] = d[v]
        elif cmd == "sub":
            d[c] -= d[v]
        elif cmd == "mul":
            d[c] *= d[v]
            self.mul_calls += 1
        elif cmd == "jnz":
            if d[c] != 0:
                self.i += d[v]
                self.progressed = True
                return

        self.i += 1
        self.progressed = True
        self.d = d

lines = open(sys.argv[1], 'r').readlines()
p0 = Program(lines, 0)

prev = None
while p0.progressed:

    p0.next()
    print(p0.i + 1, "\t", p0.d.items())
    # if prev != p0.d['h']:
    #     print(p0.d['h'], p0.i)
    #     prev = p0.d['h']
print(p0.d['h'])

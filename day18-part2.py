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
        self.d['p'] = p
        self.i = 0
        self.q = deque([])
        self.other = None
        self.progressed = True
        self.sent = 0

    def next(self):
        if self.i < 0 or self.i >= len(self.lines):
            self.progressed = False
            return

        d = self.d

        parts = lines[self.i].strip().split(" ")
        cmd = parts[0]

        if cmd == "snd":
            c = parts[1]
            self.sent += 1
            self.other.q.appendleft(d[c])
        elif cmd == "rcv":
            c = parts[1]
            if len(self.q) > 0:
                d[c] = self.q.pop()
            else:
                self.progressed = False
                return
        else:
            c, v = parts[1:]
            if cmd == "set":
                d[c] = d[v]
            elif cmd == "mul":
                d[c] *= d[v]
            elif cmd == "jgz":
                if d[c] > 0:
                    self.i += d[v]
                    self.progressed = True
                    return
            elif cmd == "mod":
                d[c] = d[c] % d[v]
            elif cmd == "add":
                d[c] += d[v]

        self.i += 1
        self.progressed = True
        self.d = d

lines = open(sys.argv[1], 'r').readlines()
p0, p1 = Program(lines, 0), Program(lines, 1)
p0.other = p1
p1.other = p0

while p0.progressed or p1.progressed:
    p0.next()
    p1.next()

print(p1.sent)

from __future__ import print_function

from collections import defaultdict


class D(defaultdict):

    def __getitem__(self, k):
        try:
            v = int(k)
            return v
        except:
            return super(D, self).__getitem__(k)


last = None
rcvd = []
skip = 0
d = D(int)

lines = open('day18-test.in', 'r').readlines()
i = 0
while i >= 0 and i < len(lines):
    parts = lines[i].strip().split(" ")
    cmd = parts[0]
    print(i, parts)

    if cmd == "snd":
        c = parts[1]
        last = d[c]
    elif cmd == "rcv":
        c = parts[1]
        if d[c] != 0:
            rcvd.append(last)
            break
    else:
        c, v = parts[1:]
        if cmd == "set":
            d[c] = d[v]
        elif cmd == "mul":
            d[c] *= d[v]
        elif cmd == "jgz":
            if d[c] > 0:
                i += d[v]
                continue
        elif cmd == "mod":
            d[c] = d[c] % d[v]
        elif cmd == "add":
            d[c] += d[v]

    i += 1

print(rcvd[0])

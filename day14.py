#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict


data = 'hfdlxzhv'
rows = []


def xor(nums):
    n = 0
    for nm in nums:
        n ^= nm
    return n


def hash2(inp):
    lens = list(map(ord, inp.strip()))
    lens += [17, 31, 73, 47, 23]
    n = 256
    A = [i for i in range(n)]
    pos = 0
    skip = 0
    for r in range(64):
        for ln in lens:
            a, b = pos, pos + ln - 1
            for i in range(ln // 2):
                A[a % n], A[b % n] = A[b % n], A[a % n]
                a += 1
                b -= 1
            pos += ln + skip
            skip += 1

    s = []
    for b in range(0, n, 16):
        s.append(xor(A[b:b+16]))
    ans = ""
    for h in s:
        ans += "{0:02x}".format(h)
    return ans

n = 0
for i in xrange(128):
    v = hash2('%s-%d' % (data, i))
    v = '{:0128b}'.format(int(v, 16))
    n += sum(map(int, v))
    rows.append(map(int, v))

print(n)

seen = set()
n = 0


def dfs(i, j):
    if ((i, j)) in seen:
        return
    if not rows[i][j]:
        return
    seen.add((i, j))
    if i > 0:
        dfs(i-1, j)
    if j > 0:
        dfs(i, j-1)
    if i < 127:
        dfs(i+1, j)
    if j < 127:
        dfs(i, j+1)

for i in range(128):
    for j in range(128):
        if (i, j) in seen:
            continue
        if not rows[i][j]:
            continue
        n += 1
        dfs(i, j)

print(n)

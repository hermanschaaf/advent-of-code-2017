from __future__ import print_function, unicode_literals


def active(r, n):
    if r == 0:
        return False

    m = n % ((r - 1) * 2)
    return m == 0

assert active(2, 0) is True
assert active(2, 1) is False
assert active(2, 2) is True
assert active(2, 3) is False

assert active(3, 0) is True
assert active(3, 1) is False
assert active(3, 2) is False
assert active(3, 3) is False
assert active(3, 4) is True
assert active(3, 5) is False

assert active(4, 0) is True
assert active(4, 1) is False
assert active(4, 2) is False
assert active(4, 3) is False
assert active(4, 4) is False
assert active(4, 5) is False
assert active(4, 6) is True
assert active(4, 7) is False

MAX = 98
d = [0 for i in range(MAX)]
while True:
    try:
        s = input().strip()
    except Exception as e:
        break
    p, r = map(int, map(str.strip, s.split(":")))
    d[p] = r

# part 1
ans = 0
for i in range(MAX):
    if active(d[i], i):
        ans += i * d[i]
print(ans)

# part 2
steps = 0
while True:
    ans = 0
    for i in range(steps, steps + MAX):
        if active(d[i-steps], i):
            ans += i * d[i-steps]
    if ans == 0:
        break
    steps += 1
    if steps % 10000 == 0:
        print(steps)
print(steps)

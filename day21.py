from collections import defaultdict, namedtuple

pattern = [".#.",
           "..#",
           "###"]
filename = 'day21.in'
rules = {}


def tostr(mat):
    return "".join(mat)


def add(src, tgt):
    global rules

    rules[tostr(src)] = tgt
    for i in range(3):
        src = ["".join(r) for r in zip(*src[::-1])]
        rules[tostr(src)] = tgt

        flip = src[::-1]
        rules[tostr(flip)] = tgt


def zoom(pattern, level=5):
    if level == 0:
        return pattern

    l = len(pattern)
    if l % 2 == 0:
        s = 2
        newl = (l // 2) * 3
    else:
        s = 3
        newl = (l // 3) * 4
    newp = [["" for c in range(newl)] for r in range(newl)]

    n = l // s
    for br in range(n):
        for bc in range(n):
            p = []
            for r in range(s):
                for c in range(s):
                    p.append(pattern[br * s + r][bc * s + c])
            rule = rules["".join(p)]
            for r in range(s + 1):
                for c in range(s + 1):
                    newp[br * (s+1) + r][bc * (s+1) + c] = rule[r][c]

    return zoom(newp, level-1)

for line in open(filename, 'r'):
    parts = line.strip().split(" ")
    src, tgt = parts[0].split("/"), parts[2].split("/")
    add(src, tgt)

newp = zoom(pattern)
cnt = sum(1 for r in newp for c in r if c == "#")
print('Part 1:', cnt)

newp = zoom(pattern, level=18)
cnt = sum(1 for r in newp for c in r if c == "#")
print('Part 2:', cnt)

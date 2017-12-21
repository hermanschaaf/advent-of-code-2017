from collections import namedtuple, defaultdict


class Particle(object):

    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def get(self, ind):
        if ind == 0:
            return self.p
        elif ind == 1:
            return self.v
        elif ind == 2:
            return self.a

Point = namedtuple('Point', 'x y z')


def manhattan(point):
    return abs(point.x) + abs(point.y) + abs(point.z)

particles = []

infile = 'day20.in'
best = None
for line in open(infile, 'r'):
    parts = line.lower().strip().split(' ')
    ar = []
    for p in parts:
        p = p.strip(",pva<>=")
        x, y, z = map(int, p.split(','))
        ar.append(Point(x, y, z))
    particle = Particle(p=ar[0], v=ar[1], a=ar[2])
    particles.append(particle)
    if best is None:
        best = particle
    else:
        i = 2
        mp, mb = 0, 0
        while mp == mb:
            mp, mb = manhattan(particle.get(i)), manhattan(best.get(i))
            i -= 1
            if i < 0:
                break

        if mp < mb:
            best = particle

print("Part 1:", particles.index(best))
conv = 10000
i = 0
prev = len(particles)
while True:
    s = defaultdict(list)
    d = set()
    for p in particles:
        p.v = Point(p.v.x + p.a.x, p.v.y + p.a.y, p.v.z + p.a.z)
        p.p = Point(p.p.x + p.v.x, p.p.y + p.v.y, p.p.z + p.v.z)

        s[p.p].append(p)
        if len(s[p.p]) == 2:
            d.add(p.p)

    for pos in d:
        for part in s[pos]:
            particles.remove(part)

    if len(particles) < prev:
        prev = len(particles)
        i = 0
    elif i >= conv:
        break
    else:
        i += 1

print("Part 2:", len(particles))

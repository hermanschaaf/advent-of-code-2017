class Circle(object):

    def __init__(self, values):
        self.head = 0
        self.A = values
        self.m = len(values)

    def spin(self, n):
        self.head = (self.head - n) % self.m

    def exchange(self, a, b):
        a = (self.head + a) % self.m
        b = (self.head + b) % self.m
        self.A[a], self.A[b] = self.A[b], self.A[a]

    def partner(self, a, b):
        ia, ib = self.A.index(a), self.A.index(b)
        self.A[ia], self.A[ib] = self.A[ib], self.A[ia]

    def __repr__(self):
        return "".join(self.A[self.head:self.m] + self.A[0:self.head])

chars = 'abcdefghijklmnop'
# chars = 'abcde'
cmds = input().strip().split(",")


def dance(circle, cmds, iterations=1):
    seen = {}
    found = False
    i = 0
    while True:
        if i >= iterations:
            break

        for cmd in cmds:
            t = cmd[0]
            if t == 's':
                n = int(cmd[1:])
                circle.spin(n)
            elif t == 'x':
                a, b = map(int, cmd[1:].split("/"))
                circle.exchange(a, b)
            elif t == 'p':
                a, b = cmd[1:].split("/")
                circle.partner(a, b)
            else:
                raise Exception("unknown {}".format(cmd))

        if not found:
            v = str(circle)
            if v in seen:
                cycle_len = i - seen[v]
                i += cycle_len * ((iterations - i) // cycle_len)
                found = True
            else:
                seen[v] = i

        i += 1

    return circle

circle = Circle(list(chars))
print("Part1:", dance(circle, cmds))

circle = Circle(list(chars))
print("Part2:", dance(circle, cmds, 1000000000))

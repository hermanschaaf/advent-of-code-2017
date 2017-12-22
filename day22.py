from collections import defaultdict, namedtuple

Pos = namedtuple('Pos', 'x y')

filename = 'day22.in'


class InfiniteGrid(object):
    """An infinite grid centered around an origin point"""

    def __init__(self, default_val=None):
        self.mat = [[default_val]]
        self.rows = 1
        self.cols = 1
        self.origin = Pos(0, 0)
        self.default_val = default_val

    def _expand(self):
        # double size of grid in transparent manner
        new_rows = self.rows * 2
        new_cols = self.cols * 2
        new_origin = Pos(new_cols // 2, new_rows // 2)
        new_mat = [[self.default_val for c in range(new_cols)] for r in range(new_rows)]

        for y in range(self.rows):
            for x in range(self.cols):
                old_val = self.mat[y][x]
                new_mat[new_origin.y + y - self.origin.y][new_origin.x + x - self.origin.x] = old_val

        self.rows = new_rows
        self.cols = new_cols
        self.origin = new_origin
        self.mat = new_mat

    def _pos(self, x, y):
        nx = self.origin.x + x
        if nx < 0 or nx >= self.cols:
            return None

        ny = self.origin.y + y
        if ny < 0 or ny >= self.rows:
            return None

        return Pos(nx, ny)

    def get(self, x, y):
        pos = self._pos(x, y)
        if pos is None:
            return None

        return self.mat[pos.y][pos.x]

    def set(self, x, y, val):
        pos = self._pos(x, y)
        while pos is None:
            self._expand()
            pos = self._pos(x, y)
        self.mat[pos.y][pos.x] = val

    def __repr__(self):
        s = []
        for row in self.mat:
            s.append("".join((c if c else '.' for c in row)))
        return "\n".join(s)


def load():
    grid = InfiniteGrid()
    with open(filename, 'r') as f:
        r = 0
        for line in f:
            line = line.strip()
            s = len(line)
            for c, v in enumerate(line):
                if v == "#":
                    grid.set(c - s // 2, r - s // 2, v)
            r += 1
    return grid

# part 1
grid = load()
pos = Pos(0, 0)
dirs = [
    Pos(0, -1),  # up
    Pos(1, 0),  # right
    Pos(0, 1),  # down
    Pos(-1, 0)  # left
]
d = 0
cnt = 0
for i in range(10000):
    v = grid.get(pos.x, pos.y)
    if v == '#':
        d = (d + 1) % 4
        grid.set(pos.x, pos.y, '.')
    else:
        d = (d - 1) % 4
        grid.set(pos.x, pos.y, '#')
        cnt += 1
    pos = Pos(pos.x + dirs[d].x, pos.y + dirs[d].y)

print("Part 1", cnt)

# part 2
grid = load()
pos = Pos(0, 0)
dirs = [
    Pos(0, -1),  # up
    Pos(1, 0),  # right
    Pos(0, 1),  # down
    Pos(-1, 0)  # left
]
d = 0
cnt = 0
for i in range(10000000):
    v = grid.get(pos.x, pos.y)
    if v == '#':  # infected
        d = (d + 1) % 4
        grid.set(pos.x, pos.y, 'f')
    elif v == 'f':  # flagged
        d = (d - 2) % 4
        grid.set(pos.x, pos.y, '.')
    elif v == 'w':  # weakened
        grid.set(pos.x, pos.y, '#')
        cnt += 1
    else:  # clean
        d = (d - 1) % 4
        grid.set(pos.x, pos.y, 'w')
    pos = Pos(pos.x + dirs[d].x, pos.y + dirs[d].y)

print("Part 1", cnt)

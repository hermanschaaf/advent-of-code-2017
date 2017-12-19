dirs = {
    'D': (1, 0),  # down
    'L': (0, -1),  # left
    'R': (0, 1),  # right
    'U': (-1, 0),  # up
}

opp = {
    'D': ['L', 'R'],
    'U': ['L', 'R'],
    'R': ['U', 'D'],
    'L': ['U', 'D'],
}

char = {
    'D': '|',
    'U': '|',
    'L': '-',
    'R': '-',
}


def get(lines, r, c):
    if r < 0 or r >= len(lines):
        return None
    if c < 0 or c >= len(lines[0]):
        return None
    return lines[r][c]

found = []
steps = 0
if __name__ == '__main__':
    with open('day19.in') as f:
        lines = [l.strip("\n") for l in f.readlines()]
        i = lines[0].find("|")
        r, c = 0, i
        d = 'D'
        while True:
            r, c = r + dirs[d][0], c + dirs[d][1]
            steps += 1
            ch = lines[r][c]
            if ch in ("|", "-"):
                continue
            elif ch == "+":
                for mv in opp[d]:
                    nr, nc = r + dirs[mv][0], c + dirs[mv][1]
                    if lines[nr][nc] == char[mv] or lines[nr][nc].isalpha():
                        r, c = nr, nc
                        steps += 1
                        d = mv
                        break
                else:
                    raise Exception("Not found:", r, c)
            elif ch.isalpha():
                found.append(ch)
            else:
                break
print("".join(found))
print(steps)


steps = 312

A = [0]
pos = 0
for i in range(1, 2018):
    m = len(A)
    pos = (pos + steps) % m
    if pos == 0:
        pos = m
    A.insert(pos, i)
    pos += 1
print("Part 1:", A[pos])


first = []
pos = 0
m = 1
for i in range(1, 50000001):
    pos = (pos + steps) % m
    if pos == 0:
        pos = m
    m += 1
    if pos == 1:
        first.append(i)
    pos += 1
print("Part 2:", first[-1])

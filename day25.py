import re

from collections import defaultdict, namedtuple

begin = re.compile(r'Begin in state (?P<begin>[A-Z])\.')
diagn = re.compile(r'Perform a diagnostic checksum after (?P<number>\d+) steps\.')
state = re.compile(r'In state (?P<state>[A-Z])\:')
curvl = re.compile(r'\s*If the current value is (?P<val>\d)\:')
wrtvl = re.compile(r'\s*\- Write the value (?P<val>\d)\.')
mvdir = re.compile(r'\s*\- Move one slot to the (?P<dir>left|right)\.')
mvstt = re.compile(r'\s*\- Continue with state (?P<state>[A-Z])\.')


class Rule(object):
    def __init__(self, write, movedir, newstate):
        self.write = write
        self.movedir = movedir
        self.newstate = newstate

    def __repr__(self):
        return "{} {} {}".format(self.write, self.movedir, self.newstate)

rules = {}

filename= 'day25.in'
with open(filename) as f:
    initial = begin.match(f.readline()).group(1)
    # print(initial)

    steps = int(diagn.match(f.readline()).group(1))
    # print(steps)

    while True:
        line = f.readline()
        if line == "":
            break

        start = state.match(f.readline()).group(1)
        if1 = int(curvl.match(f.readline()).group(1))
        wrt1 = int(wrtvl.match(f.readline()).group(1))
        mvd1 = mvdir.match(f.readline()).group(1)
        mvst1 = mvstt.match(f.readline()).group(1)
        rule1 = Rule(wrt1, mvd1, mvst1)

        if2 = int(curvl.match(f.readline()).group(1))
        wrt2 = int(wrtvl.match(f.readline()).group(1))
        mvd2 = mvdir.match(f.readline()).group(1)
        mvst2 = mvstt.match(f.readline()).group(1)
        rule2 = Rule(wrt2, mvd2, mvst2)
        
        assert if1 == 0
        assert if2 == 1

        rules[start] = [rule1, rule2]

    s = initial
    ar = [0 for i in range(steps * 2)]
    pos = steps / 2
    for i in range(steps):
        rule = rules[s]
        r = rule[ar[pos]]
        ar[pos] = r.write
        if r.movedir == "left":
            pos -= 1
        else:
            pos += 1
        s = r.newstate

    # print(rules)
    print(sum(ar))
#!/bin/python

from __future__ import print_function, unicode_literals

import re
from collections import defaultdict

re_line = re.compile(r'^(?P<name>\w+) (?P<value>\(\d+\))(?: -> )?(?P<children>[\w\s\,]+)?$')


class Node(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []
        self.parents = []

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)

    def solve(self):
        counts = defaultdict(list)
        for child in self.children:
            v = child.solve()
            counts[v].append(child)

        if len(counts) > 1:
            good_apple, bad_apple = None, None
            for v, ch in counts.items():
                if len(ch) > 1:
                    good_apple = v
                else:
                    bad_apple = v
            print(counts[good_apple][0].sum - counts[bad_apple][0].sum + counts[bad_apple][0].value)
            counts[good_apple] += counts[bad_apple]
            counts[bad_apple] = []

        self.sum = self.value + sum((v * len(ch) for v, ch in counts.items()))
        return self.sum

    def __repr__(self):
        return self.name

if __name__ == "__main__":
    nodes = {}
    while True:
        try:
            line = input().strip()
            groups = re_line.search(line).groupdict()

            name, value = groups['name'], groups['value']
            if name not in nodes:
                nodes[name] = Node(name, int(value.strip("()")))
            else:
                nodes[name].value = int(value.strip("()"))

            if groups['children']:
                children = list(map(str.strip, groups['children'].split(",")))
                for child in children:
                    if child not in nodes:
                        nodes[child] = Node(name=child, value=None)
                    nodes[name].add_child(nodes[child])
        except Exception as e:
            # print(e)
            break
    root = None
    for name, node in nodes.items():
        # print(node.name, node.value)
        if len(node.parents) == 0:
            root = node

    print("Part 1:", root.name)
    print("Part 2:", end=" ")
    root.solve()

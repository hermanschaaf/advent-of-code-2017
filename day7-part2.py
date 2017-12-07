#!/bin/python

from __future__ import print_function, unicode_literals

import math
import re
from collections import defaultdict

re_line = re.compile(r'^(?P<name>\w+) (?P<value>\(\d+\))(?: -> )?(?P<children>[\w\s\,]+)?$')


class Node(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []
        self.parents = []

        self.reset()

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)

    def reset(self):
        self.discovered = False
        self.processed = False
        self.earliest = math.inf

    def solve(self):
        vals = []
        for child in self.children:
            vals.append(child.solve())

        self.sum = self.value + sum(vals)
        if len(set(vals)) != 1:
            print(self.name, vals)
            return self.sum
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

            print(e)
            break
    root = None
    for name, node in nodes.items():
        print(node.name, node.value)
        if len(node.parents) == 0:
            root = node

    print("Part 1:", root.name)
    print("Part 2:", root.solve())

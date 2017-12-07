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
                nodes[name] = Node(name, value)
            else:
                nodes[name].value = value

            if groups['children']:
                children = list(map(str.strip, groups['children'].split(",")))
                for child in children:
                    if child not in nodes:
                        nodes[child] = Node(name=child, value=None)
                    nodes[name].add_child(nodes[child])
        except Exception as e:

            print(e)
            break

    for name, node in nodes.items():
        if len(node.parents) == 0:
            print(node.name)

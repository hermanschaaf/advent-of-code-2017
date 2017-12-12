#!/bin/python

from __future__ import print_function, unicode_literals

from collections import defaultdict


class Node(object):

    def __init__(self, value):
        self.value = value
        self.adjacent = []
        self.reset()

    def reset(self):
        self.visited = False
        self.number = 0

    def count(self, num=0):
        cnt = 1
        self.visited = True
        self.number = num
        for node in self.adjacent:
            if not node.visited:
                node.visited = True
                cnt += node.count(num=num)
        return cnt


def count_groups(nodes):
    for node in nodes:
        node.reset()

    cnt = 1
    for node in nodes:
        if node.number == 0:
            node.count(cnt)
            cnt += 1
    return cnt - 1

if __name__ == "__main__":
    nodes = []
    adjacency = []
    while True:
        try:
            s = input().strip()
            sep = " <-> "
            ind = s.index(sep)
            id, adj = int(s[:ind]), list(map(int, map(str.strip, s[ind+len(sep):].split(","))))
            nodes.append(Node(id))
            adjacency.append(adj)
        except:
            break
    for r, row in enumerate(adjacency):
        nodes[r].adjacent = [nodes[i] for i in row]
    print(nodes[0].count())
    print(count_groups(nodes))

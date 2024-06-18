#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clone Graph.

https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1392/
Created on Mon Jun 17 08:18:21 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from timer import timer


class Node:  # Neighbors
    """Implementation for Clone Graph."""

    def __init__(self, val: int):
        self.val = val
        self.neighbors: list[Node] = []

    def __repr__(self) -> str:
        represented = []
        stack = deque([self])
        while stack:
            cur = stack.pop()
            represented.append(cur)
            for neighbor in cur.neighbors:
                if neighbor not in represented:
                    stack.append(neighbor)

        res = []
        for node in represented:
            neighbors = []
            for neighbor in node.neighbors:
                neighbors.append(neighbor.val)
            res.append(f"{node.val}: {str(neighbors)}")

        return f"<Node {id(self)}: {str(res)}>"

    @staticmethod
    def create(source: list[list[int]]) -> 'Node':
        """Create nodes graph."""
        nodes: dict[int, Node] = {}
        for key in range(1, len(source)+1):
            nodes[key] = Node(key)

        for key, vals in enumerate(source, start=1):
            for val in vals:
                nodes[key].neighbors.append(nodes[val])

        return nodes[1]


class Solution:
    """Leetcode class for answers."""

    def cloneGraph(self,  # pylint: disable=invalid-name
                   node: Node | None) -> Node | None:
        """Leetcode function as answer."""
        if node is None:
            return None
        head = Node(node.val)
        nodes = {node: head}
        stack: deque[tuple[Node, Node]] = deque([(head, node)])
        while stack:
            new, old = stack.pop()
            for old_neighbor in old.neighbors:
                new_neighbor = nodes.get(old_neighbor, None)
                if new_neighbor is None:
                    new_neighbor = Node(old_neighbor.val)
                    nodes[old_neighbor] = new_neighbor
                    stack.append((new_neighbor, old_neighbor))
                new.neighbors.append(new_neighbor)
        return head


if __name__ == "__main__":
    graph = Node.create([[2, 4], [1, 3], [2, 4], [1, 3]])
    print(graph)
    func_timed = timer(Solution().cloneGraph)
    print("result:", func_timed(graph))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    def assert_node(node1: Node, node2: Node | None) -> None:
        assert node1 != node2
        assert len(node1.neighbors) == 2
        assert node2 is not None
        assert len(node2.neighbors) == 2
        assert node1.neighbors[0] != node2.neighbors[0]
        assert node1.neighbors[1] != node2.neighbors[1]

    node11 = Node.create([[2, 4], [1, 3], [2, 4], [1, 3]])
    node12 = Solution().cloneGraph(node11)
    assert_node(node11, node12)

    node21 = node11.neighbors[0]
    assert node12 is not None
    node22 = node12.neighbors[0]
    assert_node(node21, node22)

    node31 = node21.neighbors[0]
    assert node22 is not None
    node32 = node22.neighbors[0]
    assert_node(node31, node32)

    node41 = node31.neighbors[0]
    assert node32 is not None
    node42 = node32.neighbors[0]
    assert_node(node41, node42)


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().cloneGraph(
           None) is None

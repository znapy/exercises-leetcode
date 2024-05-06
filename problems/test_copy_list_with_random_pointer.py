#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copy List with Random Pointer.

https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/
Created on Sun May  5 08:19:13 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Node:
    """Leetcodes structure named Node."""

    def __init__(self, x: int, next_: ['Node', None] = None,
                 random: ['Node', None] = None) -> None:
        self.val = int(x)
        self.next = next_
        self.random = random


class Convertor:
    """Helps to test the unswer."""

    @staticmethod
    def _representation_linked_nodes(node: Node | None) -> str:
        """Print a structure, created in list_to_nodes."""
        def with_rand(node: Node | None) -> str:
            cur_text = ""
            cur_node: Node | None = node
            while cur_node:
                cur_text += (" -> " if cur_text else "")\
                         + str(cur_node.val)
                if cur_node.random:
                    cur_text += f"({cur_node.random.val})"
                cur_node = cur_node.next
            return cur_text

        return with_rand(node)


class Solution:
    """Leetcode class for answers."""

    def copyRandomList(self, head: Node | None) -> Node | None:
        """Leetcode function as answer."""
        if head is None:
            return None

        result = Node(head.val, head.next, head.random)
        assoc: dict[Node, Node] = {head: result}
        current = head.next
        while current:
            assoc[current] = Node(current.val, current.next, current.random)
            current = current.next

        current = result
        while current:
            if current.next is not None:
                current.next = assoc[current.next]
            if current.random is not None:
                current.random = assoc[current.random]
            current = current.next

        return result


if __name__ == "__main__":
    astext = Convertor._representation_linked_nodes
    func_timed = timer(Solution().copyRandomList)

    h = Node(1)
    h.next = Node(2)
    h.next.random = h
    print("task:", astext(h), sep="\n")
    c = Solution().copyRandomList(h)
    print("result:", astext(func_timed(c)))
    print("h.next == c.next:", h.next == c.next)  # type: ignore[union-attr]

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    func = Solution().copyRandomList
    astext = Convertor._representation_linked_nodes

    node5 = Node(1)
    node4 = Node(10, node5)
    node3 = Node(11, node4)
    node2 = Node(13, node3)
    node1 = Node(7, node2)

    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    result = func(node1)
    assert astext(result) == \
        "7 -> 13(7) -> 11(1) -> 10(11) -> 1(7)"
    assert result != node1


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    func = Solution().copyRandomList
    astext = Convertor._representation_linked_nodes

    node2 = Node(2)
    node2.random = node2
    node1 = Node(1, node2, node2)

    result = func(node1)
    assert astext(result) == \
        "1(2) -> 2(2)"
    assert result != node1


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    func = Solution().copyRandomList

    node3 = Node(3)
    node2 = Node(3, node3)
    node1 = Node(3, node2)

    node2.random = node1

    result = func(node1)
    assert result != node1
    assert result.random is None         # type: ignore[union-attr]
    assert result.next.random == result  # type: ignore[union-attr]
    assert result.next.next.random is None

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flatten a Multilevel Doubly Linked List.

https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/
Created on Sat May  4 11:14:03 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Node:
    """Leetcodes structure named Node."""

    def __init__(self, val: int, prev: ['Node', None],
                 next_: ['Node', None], child: ['Node', None]) -> None:
        self.val = val
        self.prev = prev
        self.next = next_
        self.child = child


class Convertor:
    """Helps to test the unswer."""

    @staticmethod
    def add_as_next(node: Node, val: int) -> Node:
        """Add value as next node."""
        old = node.next
        new_node = Node(val, node, old, None)
        if old is not None:
            old.prev = new_node
        node.next = new_node
        return new_node

    @staticmethod
    def list_to_nodes(serialized: list[int | None]) -> Node:
        """Convert serialised list to nodes."""
        heads: list[Node] = []
        current: Node | None = None
        parent: Node | None = None
        for val in serialized:

            if val:
                if current is None:
                    current = Node(val, None, None, None)
                    heads.append(current)
                else:
                    current = Convertor.add_as_next(current, val)

                if parent:
                    parent.child = current
                    parent = None

                continue

            if parent:
                parent = parent.next
            if current:
                parent = heads[-1]
                current = None

        if len(heads) == 0:
            raise ValueError("Serialised list should have not None value")
        return heads[0]

    @staticmethod
    def _representation_linked_nodes(node: Node | None) -> str:
        """Print a structure, created in list_to_nodes."""
        def with_child(node: Node | None) -> str:
            child: Node | None = None
            cur_text = ""
            cur_node = node
            result: list[str] = []
            while cur_node:
                cur_text += (" -> " if cur_text else "")\
                         + str(cur_node.val)
                if cur_node.child:
                    child = cur_node.child
                    cur_text += "(+)"
                cur_node = cur_node.next
                if cur_node is None:
                    result.append(cur_text)
                    cur_text = ""
                    cur_node = child
                    child = None
            return "\n".join(result)

        return with_child(node)


class Solution:
    """Leetcode class for answers."""

    def _set_next(self, node: Node) -> Node:
        """Change next links to eliminate childs recursively."""
        old: Node | None = None
        if node.child:
            old = node.next
            node.next = node.child
            node.next.prev = node
            node.child = None

        if node.next is None:
            return node
        from_recursion = self._set_next(node.next)
        if old:
            from_recursion.next = old
            old.prev = from_recursion
            return self._set_next(old)
        return from_recursion

    def flatten(self, head: Node | None) -> Node | None:
        """Leetcode function as answer."""

        if head is None:
            return None
        self._set_next(head)
        return head


if __name__ == "__main__":
    astext = Convertor._representation_linked_nodes
    ser = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12]
    head = Convertor.list_to_nodes(ser)
    print("task:", astext(head), sep="\n")

    func_timed = timer(Solution().flatten)
    print("result:", astext(func_timed(head)))

#########
# Tests
# pylint: disable=missing-function-docstring


class TestConvertor:
    """Test convertor's methods."""

    def test_add_as_next(self) -> None:
        """Check add_as_next function."""
        func = Convertor.add_as_next

        node = Node(1, None, None, None)
        res1 = func(node, 3)
        assert node.prev is None
        assert node.child is None
        assert node.val == 1
        assert node.next is not None
        assert node != res1
        assert node.next == res1
        assert res1.prev == node
        assert res1.child is None
        assert res1.val == 3
        assert res1.next is None

        res2 = func(node, 2)
        assert node.prev is None
        assert node.child is None
        assert node.val == 1
        assert node.next is not None
        assert node != res1
        assert node.next == res2
        assert res2.prev == node
        assert res2.child is None
        assert res2.val == 2
        assert res2.next == res1
        assert res1.prev == res2

    def test_list_to_nodes(self) -> None:
        """Test list_to_nodes function."""
        func = Convertor.list_to_nodes
        astext = Convertor._representation_linked_nodes

        assert astext(func([1])) == "1"

        assert astext(func([1, 2])) == "1 -> 2"

        assert astext(func([1, 2, None, 3])) == "1(+) -> 2\n3"

        assert astext(func([1, None, 2, 3])) == "1(+)\n2 -> 3"

        assert astext(func([1, 2, None, None, 3])) == "1 -> 2(+)\n3"

        # leetcodes example
        ser = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10] +\
              [None, None, 11, 12]
        etalon = "1 -> 2 -> 3(+) -> 4 -> 5 -> 6\n"\
                 "7 -> 8(+) -> 9 -> 10\n"\
                 "11 -> 12"
        assert astext(func(ser)) == etalon


class TestSolution:
    """Test class."""

    @staticmethod
    def _check_next_prev(node: Node) -> None:
        """Check if next (recursive) is exist - its prev should be setted."""
        if node.next:
            assert node.next.prev == node
            TestSolution._check_next_prev(node.next)

    @staticmethod
    def test_flatten() -> None:
        """Leetcode and my testcases."""
        s = Solution()
        list_to_nodes = Convertor.list_to_nodes
        astext = Convertor._representation_linked_nodes

        # leetcodes example 1
        ser = list_to_nodes([1, 2, 3, 4, 5, 6, None, None, None] +
                            [7, 8, 9, 10, None, None, 11, 12])
        etalon = "1 -> 2 -> 3 -> 7 -> 8 -> 11 -> 12 -> 9 -"\
                 "> 10 -> 4 -> 5 -> 6"
        assert astext(s.flatten(ser)) == etalon
        TestSolution._check_next_prev(ser)

        # leetcodes example 2
        ser = list_to_nodes([1, 2, None, 3])
        etalon = "1 -> 3 -> 2"
        res = s.flatten(ser)
        assert astext(res) == etalon
        assert res.child is None     # type: ignore[union-attr]
        assert res.next.prev == res  # type: ignore[union-attr]
        assert res.next.next.prev == res.next

        # leetcodes example 3
        assert s.flatten(None) is None

        node = Node(1, None, None, None)
        assert astext(s.flatten(node)) == "1"

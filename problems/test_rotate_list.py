#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rotate List.

https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
Created on Mon May  6 09:45:54 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x: [int, 'ListNode'], next_: ["ListNode", None] = None
                 ) -> None:
        self.val = x
        self.next: ListNode | None = next_

    def __repr__(self) -> str:
        """Representation of object is [head -> val -> tail]."""
        current = self
        result = str(current.val)
        nodes: list[ListNode] = [current]
        while current.next is not None and\
                nodes.count(current.next) == 0:

            current = current.next
            nodes.append(current)
            result += " -> " + str(current.val)

        if current.next is not None and\
           nodes.count(current.next):
            result += " -> ...looped to " + str(current.next.val)

        return "<ListNode: [" + result + "]>"


class Solution:
    """Leetcode class for answers."""

    def rotateRight(self,  # pylint: disable=invalid-name
                    head: ListNode | None, k: int) -> ListNode | None:
        """Leetcode function as answer."""
        if head is None:
            return None
        if k == 0:
            return head

        current = head
        length = 1
        while current.next:
            length += 1
            current = current.next

        steps = k % length
        if steps == 0:
            return head

        current.next = head
        current = head
        # steps if we will go to stright
        steps = length - steps

        while True:
            steps -= 1
            if steps == 0:
                result = current.next
                current.next = None
                return result
            current = current.next  # type: ignore[assignment] # Why it warns?

        raise ValueError("Unknown error")


if __name__ == "__main__":
    func_timed = timer(Solution().rotateRight)
    h = ListNode(1, ListNode(2))
    print("result:", func_timed(h, 1))

#########
# Tests
# pylint: disable=missing-function-docstring


class TestSolution:
    """Test class."""

    @staticmethod
    def test_rotateRight() -> None:  # pylint: disable=invalid-name
        """Leetcode and my testcases."""
        func = Solution().rotateRight

        node0 = ListNode(0)
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)

        # Leetcode example 1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        assert str(func(node1, 2)) == "<ListNode: [4 -> 5 -> 1 -> 2 -> 3]>"

        # Leetcode example 2
        node0.next = node1
        node1.next = node2
        node2.next = None
        assert str(func(node0, 4)) == "<ListNode: [2 -> 0 -> 1]>"

        assert func(None, 0) is None

        node1.next = None
        assert func(node1, 0) == node1
        assert func(node1, 1) == node1
        assert func(node1, 2) == node1

        node1.next = node2
        node2.next = None
        assert func(node1, 0) == node1

        head = func(node1, 2)
        assert head == node1

        head = func(head, 1)
        assert head == node2
        assert head.next == node1
        assert head.next.next is None

        head = func(head, 3)
        assert head == node1
        assert head.next == node2
        assert head.next.next is None

        node2.next = node3
        node3.next = None
        head = func(head, 1)
        assert head == node3

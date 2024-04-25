#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linked List Cycle.

https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/
Created on Tue Apr 23 20:58:24 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x: int) -> None:
        self.val = x
        self.next: ListNode | None = None

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

    def hasCycle(self, head: ListNode | None) -> bool:
        """
        Linked List Cycle.

        https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/
        """
        if head is None or head.next is None:
            return False

        current = head
        faster = current.next
        for _ in range(9999):
            if current == faster:
                return True
            current = current.next
            faster = faster.next
            if faster is None or faster.next is None:
                return False
            if current == faster:
                return True
            faster = faster.next

        return False


if __name__ == "__main__":
    func_timed = timer(Solution().hasCycle)
    head = ListNode(1)
    print("result:", func_timed(head))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    node4 = ListNode(-4)
    node3 = ListNode(0)
    node3.next = node4
    node2 = ListNode(2)
    node2.next = node3
    node4.next = node2
    head = ListNode(3)
    head.next = node2
    assert Solution().hasCycle(head) is True


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert Solution().hasCycle(head) is True


def test_leetcode_example_3() -> None:
    """The fird example in the task."""
    head = ListNode(1)
    assert Solution().hasCycle(head) is False


def test_changed_chain() -> None:
    func = Solution().hasCycle

    assert func(None) is False

    head = ListNode(1)
    assert func(head) is False

    head.next = ListNode(2)
    assert func(head) is False

    head.next.next = head
    assert func(head) is True

    head.next.next = head.next
    assert func(head) is True

    head.next.next = ListNode(3)
    assert func(head) is False

    head.next.next.next = head.next
    assert func(head) is True

    head.next.next.next = head.next.next
    assert func(head) is True

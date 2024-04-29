#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverse Linked List.

https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/
Created on Sun Apr 28 12:18:09 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x: [int, 'ListNode']) -> None:
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

    def reverseList(self,
                    head: ListNode | None) -> ListNode | None:
        """Leetcode function as answer."""
        if head is None:
            return head

        pointer, head.next = head.next, None
        while pointer is not None:
            pointer.next, pointer, head = \
                head, pointer.next, pointer

        return head


if __name__ == "__main__":
    func_timed = timer(Solution().reverseList)
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print("result:", func_timed(head))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    func = Solution().reverseList

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    res = func(a)
    assert res == e
    assert e.next == d
    assert d.next == c
    assert c.next == b
    assert b.next == a
    assert a.next is None


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    func = Solution().reverseList

    a = ListNode(1)
    b = ListNode(2)

    a.next = b
    b.next = None
    res = func(a)
    assert res == b
    assert b.next == a
    assert a.next is None

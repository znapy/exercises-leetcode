#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intersection of Two Linked Lists.

https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/
Created on Fri Apr 26 08:25:33 2024
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

    def getIntersectionNode(self,
                            headA: ListNode,
                            headB: ListNode) -> ListNode | None:
        """Leetcode function as answer."""
        backA = ListNode(headA)
        backB = ListNode(headB)
        currentA = headA
        currentB = headB
        while True:
            stop = True
            if currentA.next is not None:
                currentA = currentA.next
                backA, backA.next = ListNode(currentA), backA
                stop = False
            if currentB.next is not None:
                currentB = currentB.next
                backB, backB.next = ListNode(currentB), backB
                stop = False
            if stop:
                break

        if currentA != currentB:
            return None

        while True:
            if backA.next is not None and\
               backB.next is not None and\
               backA.next.val == backB.next.val:
                backA = backA.next
                backB = backB.next
            else:
                break

        return backA.val
        # another solution:
        # if headA is A+X (X is the common part)
        # and headB is B+X than two-pointers solution is loop
        # throw AXBX and throw BXAX - the second X started
        # at the same time


if __name__ == "__main__":
    func_timed = timer(Solution().getIntersectionNode)
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = headA.next.next
    print("result:", func_timed(headA, headB))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    func = Solution().getIntersectionNode

    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = headA.next.next
    assert func(headA, headB) == headA.next.next


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    func = Solution().getIntersectionNode

    headA = ListNode(1)
    headA.next = ListNode(9)
    headA.next.next = ListNode(1)
    headA.next.next.next = ListNode(2)
    headA.next.next.next.next = ListNode(4)
    headB = ListNode(3)
    headB.next = headA.next.next.next
    assert func(headA, headB) == headA.next.next.next


def test_leetcode_example_3() -> None:
    """The fird example in the task."""
    func = Solution().getIntersectionNode

    headA = ListNode(2)
    headA.next = ListNode(6)
    headA.next.next = ListNode(4)
    headB = ListNode(1)
    headB.next = ListNode(5)
    assert func(headA, headB) is None


def test_changed_chain() -> None:
    func = Solution().getIntersectionNode

    headA = ListNode(1)
    headB = ListNode(1)
    assert func(headA, headB) is None

    assert func(headA, headA) == headA

    headB.next = headA
    assert func(headA, headB) == headA

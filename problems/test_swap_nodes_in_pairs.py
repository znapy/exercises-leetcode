#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Swap Nodes in Pairs.

https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1681/
Created on Wed May  8 08:25:23 2024
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

    @staticmethod
    def construct(vals: list[int]) -> 'ListNode':
        """
        Construct linked nodes from list.

        This is my implementation - not the leetcode interface.
        """
        head = cur = ListNode(vals[0])
        for val in vals[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head


class Solution:
    """Leetcode class for answers."""

    def swapPairs(self,  # pylint: disable=invalid-name
                  head: ListNode | None) -> ListNode | None:
        """Leetcode function as answer."""
        if head is None:
            return None
        second = head.next
        if second is None:
            return head
        second.next, head.next = head, self.swapPairs(second.next)
        return second


def main() -> None:
    """The launch function."""
    func_timed = timer(Solution().swapPairs)
    vals = ListNode.construct([1, 2, 3, 4, 5])
    print("result:", func_timed(vals))


if __name__ == "__main__":
    main()

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert str(Solution().swapPairs(ListNode.construct(
        [1, 2, 3, 4]))) == \
        "<ListNode: [2 -> 1 -> 4 -> 3]>"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().swapPairs(
        None) is \
        None


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert str(Solution().swapPairs(
        ListNode(1))) == \
        "<ListNode: [1]>"

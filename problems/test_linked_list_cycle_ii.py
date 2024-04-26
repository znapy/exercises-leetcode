#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linked List Cycle II.

https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
Created on Thu Apr 25 08:01:12 2024
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

    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        """Leetcode function as answer."""
        if head is None or head.next is None:
            return None

        # If it has loop - remember steps to "back" list
        back = ListNode(head)
        current = head
        faster = head.next
        back, back.next = ListNode(faster), ListNode(current)
        while current != faster:
            current, faster = current.next, faster.next
            back, back.next = ListNode(faster), back
            if faster is None or faster.next is None:
                return None
            if current == current.next:
                return current
            if current == faster:
                break
            faster = faster.next
            back, back.next = ListNode(faster), back

        # Throw back list find the looped node
        repeater = back
        current = back
        while current.next is not None:
            current = current.next
            if current.val == repeater.val:
                repeater = repeater.next
                if current.next is None or\
                   current.next.val != repeater.val:
                    return current.val

        return current.val
        # Best solution:
        # ----------------
        # slow = fast = head
        # while fast and fast.next:
        #     slow, fast = slow.next, fast.next.next
        #     if slow == fast: break
        # else: return None  # if not (fast and fast.next): return None
        # while head != slow:
        #     head, slow = head.next, slow.next
        # return head
        # ----------------
        # good explanation:
        # https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/discuss/1701128/C++JavaPython-Slow-and-Fast-oror-Image-Explanation-oror-Beginner-Friendly


if __name__ == "__main__":
    func_timed = timer(Solution().detectCycle)
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
    assert Solution().detectCycle(head) == node2


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert Solution().detectCycle(head) == head


def test_leetcode_example_3() -> None:
    """The fird example in the task."""
    head = ListNode(1)
    assert Solution().detectCycle(head) is None


def test_changed_chain() -> None:
    func = Solution().detectCycle

    assert func(None) is None

    head = ListNode(1)
    assert func(head) is None

    head.next = ListNode(2)
    assert func(head) is None

    head.next.next = head
    assert func(head) == head

    head.next.next = head.next
    assert func(head) == head.next

    head.next.next = ListNode(3)
    assert func(head) is None

    head.next.next.next = head.next
    assert func(head) == head.next

    head.next.next.next = head.next.next
    assert func(head) == head.next.next

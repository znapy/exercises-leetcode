#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add Two Numbers.

https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/
Created on Fri May  3 07:52:25 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer
from typing import Iterable, cast


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x: [int, 'ListNode'], next: ["ListNode", None] = None
                 ) -> None:
        self.val = x
        self.next: ListNode | None = next

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


class LinkedList:
    """
    Steroids to linked list.

    It works well, while you modify links throw this class
    """

    def __init__(self, vals: Iterable[int]) -> None:
        # A head can be None after remove the last node
        self.head: ListNode | None = None
        self.tail: ListNode | None = None
        self.size = 0

        for val in vals:
            self.add_at_tail(val)

    def add_at_head(self, val: int) -> ListNode:
        """
        Add a node of value val before the first element.

        After the insertion, the new node will be the first
        node of the linked list.
        """
        prev_head = self.head
        self.head = ListNode(val)
        self.head.next = prev_head
        self.size += 1
        if self.tail is None:
            self.tail = self.head

        return self.head

    def add_at_tail(self, val: int) -> ListNode:
        """Append a node of value val as the last element."""
        if self.tail is None:
            return self.add_at_head(val)
        node = ListNode(val)
        self.tail.next, self.tail = node, node
        self.size += 1

        return node

    def unite_with_node(self, node: ListNode) -> None:
        """Unite with node to the tail."""
        if self.tail is None:
            raise ValueError('First exemplar to unite is empty')

        self.tail.next = node
        current = node.next
        while current is not None:
            self.tail = current
            self.size += 1
            current = current.next

    def _get_node(self, index: int) -> ListNode:
        if not (0 <= index < self.size):
            raise ValueError('Index is invalid')

        current = self.head
        if current is None:
            raise ValueError("The size of list is zero")

        for i in range(index + 1):
            if i == index:
                break
            current = current.next
            if current is None:
                raise ValueError("invalid size of list")

        return current

    def __repr__(self) -> str:
        """Representation of object is [head -> val -> tail]."""
        result = ""
        current = self.head
        for i in range(self.size):
            if result:
                result += " -> "
            if current is None:
                raise ValueError("Invalid the size of list")
            result += str(i) + ": " + str(current.val)
            current = current.next

        return "<LinkedList: [" + result + "]>"


class Solution:
    """Leetcode class for answers."""

    # @staticmethod
    # def _reverse(node: ListNode) -> ListNode:
    #     cur, prev = node, None
    #     while cur.next is not None:
    #         last = cur.next
    #         cur.next = prev
    #         prev = cur
    #         cur = last
    #     cur.next = prev
    #     return cur

    @staticmethod
    def _sum(node1: ListNode | None, node2: ListNode | None
             ) -> tuple[int, ListNode | None, ListNode | None]:
        if node1 is None:
            return (node2.val, None, node2.next)  # type: ignore[union-attr]
        if node2 is None:
            return (node1.val, node1.next, None)
        return (node1.val + node2.val, node1.next, node2.next)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Leetcode function as answer."""

        node1: ListNode | None = l1
        node2: ListNode | None = l2
        prev: ListNode | None = None
        overflow = 0
        while (node1, node2) != (None, None):

            val, node1, node2 = Solution._sum(node1, node2)
            overflow, quotient = divmod(val + overflow, 10)
            node_cur = ListNode(quotient)
            if prev:
                prev.next = node_cur
            else:
                head = node_cur
            prev = node_cur

        if overflow:
            prev.next = ListNode(overflow)  # type: ignore[union-attr]

        return head


if __name__ == "__main__":
    func_timed = timer(Solution().addTwoNumbers)
    l1 = LinkedList([9]*100).head
    l2 = LinkedList([9]*100).head
    print("result:", func_timed(l1, l2))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    func = Solution().addTwoNumbers
    list1 = cast(ListNode, LinkedList([2, 4, 3]).head)
    list2 = cast(ListNode, LinkedList([5, 6, 4]).head)
    assert str(func(list1, list2)) == \
        "<ListNode: [7 -> 0 -> 8]>"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    func = Solution().addTwoNumbers
    assert str(func(ListNode(0), ListNode(0))) == \
        "<ListNode: [0]>"


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    func = Solution().addTwoNumbers
    list1 = cast(ListNode, LinkedList([9, 9, 9, 9, 9, 9, 9]).head)
    list2 = cast(ListNode, LinkedList([9, 9, 9, 9]).head)
    assert str(func(list1, list2)) == \
        "<ListNode: [8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1]>"


def test_9__0() -> None:
    func = Solution().addTwoNumbers
    assert str(func(ListNode(9), ListNode(0))) == \
        "<ListNode: [9]>"


def test_99__0() -> None:
    func = Solution().addTwoNumbers
    list1 = cast(ListNode, LinkedList([9, 9]).head)
    assert str(func(list1, ListNode(0))) == \
        "<ListNode: [9 -> 9]>"


def test_99__1() -> None:
    func = Solution().addTwoNumbers
    list1 = cast(ListNode, LinkedList([9, 9]).head)
    assert str(func(list1, ListNode(1))) == \
        "<ListNode: [0 -> 0 -> 1]>"

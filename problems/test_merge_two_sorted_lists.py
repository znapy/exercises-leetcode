#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Merge Two Sorted Lists.

https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/
Created on Thu May  2 09:20:19 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer
from typing import Iterable


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

    def _getNode(self, index: int) -> ListNode:
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

    @staticmethod
    def _get_next(node1: ListNode | None, node2: ListNode | None
                  ) -> tuple[ListNode | None,   # minimum node
                             ListNode | None,   # next node1
                             ListNode | None]:  # next node2
        if node1 is None and node2 is None:
            return None, node1, node2
        if node1 is None:
            return node2, node1, node2.next  # type: ignore[union-attr]
        if node2 is None:
            return node1, node1.next, node2
        if node1.val > node2.val:
            return node2, node1, node2.next
        return node1, node1.next, node2

    def mergeTwoLists(self,
                      list1: ListNode | None,
                      list2: ListNode | None) -> ListNode | None:
        """Leetcode function as answer."""
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        prev, node1, node2 = Solution._get_next(list1, list2)
        head = prev
        while prev is not None:
            cur, node1, node2 = Solution._get_next(node1, node2)
            prev.next = cur
            prev = cur

        return head
        # I'm lazy to realize it as recursion


if __name__ == "__main__":
    func_timed = timer(Solution().mergeTwoLists)
    list1 = LinkedList(range(50)).head
    list2 = LinkedList(range(50)).head
    print("result:", func_timed(list1, list2))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    func = Solution().mergeTwoLists
    list1 = LinkedList([1, 2, 4]).head
    list2 = LinkedList([1, 3, 4]).head
    assert str(func(list1, list2)) == \
        "<ListNode: [1 -> 1 -> 2 -> 3 -> 4 -> 4]>"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    func = Solution().mergeTwoLists
    assert func(None, None) is None


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    func = Solution().mergeTwoLists
    assert str(func(None, ListNode(0))) == \
        "<ListNode: [0]>"


def test_0__None() -> None:
    func = Solution().mergeTwoLists
    assert str(func(ListNode(0), None)) == \
        "<ListNode: [0]>"


def test_0__0() -> None:
    func = Solution().mergeTwoLists

    list1 = ListNode(0)
    list2 = ListNode(0)
    assert str(func(list1, list2)) == \
        "<ListNode: [0 -> 0]>"


def test_minus1__1() -> None:
    func = Solution().mergeTwoLists

    list1 = ListNode(-1)
    list2 = ListNode(1)
    assert str(func(list1, list2)) == \
        "<ListNode: [-1 -> 1]>"


def test_1__minus1() -> None:
    func = Solution().mergeTwoLists

    list1 = ListNode(1)
    list2 = ListNode(-1)
    assert str(func(list1, list2)) == \
        "<ListNode: [-1 -> 1]>"


def test_1_2__0() -> None:
    func = Solution().mergeTwoLists

    list1 = LinkedList([1, 2]).head
    list2 = ListNode(0)
    assert str(func(list1, list2)) == \
        "<ListNode: [0 -> 1 -> 2]>"


def test_0__1_2() -> None:
    func = Solution().mergeTwoLists

    list1 = ListNode(0)
    list2 = LinkedList([1, 2]).head
    assert str(func(list1, list2)) == \
        "<ListNode: [0 -> 1 -> 2]>"

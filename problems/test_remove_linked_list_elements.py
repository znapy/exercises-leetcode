#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove Linked List Elements.

https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
Created on Mon Apr 29 08:56:03 2024
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


class MyLinkedList:
    """
    Steroids to linked list.

    It works well, while you modify links throw this class
    """

    def __init__(self, vals: list[int]) -> None:
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

        return "<MyLinkedList: [" + result + "]>"


class Solution:
    """Leetcode class for answers."""

    def removeElements(self,
                       head: ListNode | None, val: int) -> ListNode | None:
        """Leetcode function as answer."""
        cur = head
        prev: ListNode | None = None
        while cur is not None:

            if cur.val == val:

                if prev is None:
                    head = cur.next
                else:
                    prev.next = cur.next

            if cur.val != val:
                prev = cur

            cur = cur.next

        return head


if __name__ == "__main__":
    func_timed = timer(Solution().removeElements)
    my_linked_list = MyLinkedList([1]*50)
    print("result:", func_timed(my_linked_list.head, 0))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    func = Solution().removeElements

    head = MyLinkedList([1, 2, 6, 3, 4, 5, 6]).head
    assert str(func(head, 6)) == \
        "<ListNode: [1 -> 2 -> 3 -> 4 -> 5]>"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    func = Solution().removeElements

    assert func(None, 1) is None


def test_leetcode_example_3() -> None:
    """The fird example in the task."""
    func = Solution().removeElements

    head = MyLinkedList([7, 7, 7, 7]).head
    assert func(head, 7) is None


def test_0__0() -> None:
    func = Solution().removeElements

    head = MyLinkedList([0]).head
    assert func(head, 0) is None


def test_0__1() -> None:
    func = Solution().removeElements

    head = MyLinkedList([0]).head
    assert str(func(head, 1)) == \
        "<ListNode: [0]>"


def test_remove_corners() -> None:
    func = Solution().removeElements

    head = MyLinkedList([1, 0, 1]).head
    assert str(func(head, 1)) == \
        "<ListNode: [0]>"

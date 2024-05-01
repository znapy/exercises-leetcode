#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Odd Even Linked List.

https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/
Created on Tue Apr 30 14:45:37 2024
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

    def oddEvenList(self,
                    head: ListNode | None) -> ListNode | None:
        """Leetcode function as answer."""
        if head is None:
            return None
        if head.next is None:
            return head

        odd, even = head, head.next
        head2 = even
        while even.next is not None:

            odd.next = even.next
            odd = even.next

            if odd.next is not None:

                even.next = odd.next
                even = odd.next

            else:
                even.next = None
                break

        odd.next = head2

        return head


if __name__ == "__main__":
    func_timed = timer(Solution().oddEvenList)
    my_linked_list = MyLinkedList(list(range(1, 6)))
    print("result:", func_timed(my_linked_list.head))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    func = Solution().oddEvenList

    head = MyLinkedList([1, 2, 3, 4, 5]).head
    assert str(func(head)) == \
        "<ListNode: [1 -> 3 -> 5 -> 2 -> 4]>"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    func = Solution().oddEvenList

    head = MyLinkedList([2, 1, 3, 5, 6, 4, 7]).head
    assert str(func(head)) == \
        "<ListNode: [2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4]>"


def test_None() -> None:
    func = Solution().oddEvenList

    assert func(None) is None


def test_1() -> None:
    func = Solution().oddEvenList

    head = MyLinkedList([1]).head
    assert str(func(head)) == \
        "<ListNode: [1]>"


def test_1_2() -> None:
    func = Solution().oddEvenList

    head = MyLinkedList([1, 2]).head
    assert str(func(head)) == \
        "<ListNode: [1 -> 2]>"


def test_1_2_3() -> None:
    func = Solution().oddEvenList

    head = MyLinkedList([1, 2, 3]).head
    assert str(func(head)) == \
        "<ListNode: [1 -> 3 -> 2]>"


def test_1_2_3_4() -> None:
    func = Solution().oddEvenList

    head = MyLinkedList([1, 2, 3, 4]).head
    assert str(func(head)) == \
        "<ListNode: [1 -> 3 -> 2 -> 4]>"

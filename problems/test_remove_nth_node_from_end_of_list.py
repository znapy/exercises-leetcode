#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove Nth Node From End of List.

https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/
Created on Sat Apr 27 12:30:34 2024
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

    def __init__(self, val: int) -> None:
        # A head can be None after remove the last node
        self.head: ListNode | None = None
        self.tail: ListNode | None = None
        self.size = 0
        self.add_at_head(val)

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

    def removeNthFromEnd(self,
                         head: ListNode | None,
                         n: int
                         ) -> ListNode | None:
        """Leetcode function as answer."""
        pointer_1, pointer_2 = head, head
        length, index_p2 = 0, 0
        while pointer_1 is not None:
            length += 1
            pointer_1 = pointer_1.next
            if pointer_1 is None:
                break
            length += 1
            pointer_1 = pointer_1.next

            if pointer_2 is None:
                raise ValueError("head shouldn't be empty")
            pointer_2 = pointer_2.next
            index_p2 += 1

        index_to_remove = length - n
        if index_to_remove == 0:
            if head is None is None:
                raise ValueError("parameter n is wrong")
            return head.next

        pointer_1, index_p1 = head, 0
        while index_p2 < length:
            if pointer_1 is None or pointer_2 is None:
                raise ValueError("the pointer problem 1")
            if index_p1 + 1 == index_to_remove:
                if pointer_1 is None or pointer_1.next is None:
                    raise ValueError("the pointer problem 2")
                pointer_1.next = pointer_1.next.next
                return head
            if index_p2 + 1 == index_to_remove:
                if pointer_2 is None or pointer_2.next is None:
                    raise ValueError("the pointer problem 3")
                pointer_2.next = pointer_2.next.next
                return head
            pointer_1, pointer_2 = pointer_1.next, pointer_2.next
            index_p1 += 1
            index_p2 += 1

        return head
        # another solution:
        #


if __name__ == "__main__":
    func_timed = timer(Solution().removeNthFromEnd)
    my_linked_list = MyLinkedList(1)
    my_linked_list.add_at_tail(2)
    my_linked_list.add_at_tail(3)
    print("result:", func_timed(my_linked_list.head, 3))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    func = Solution().removeNthFromEnd

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    assert str(func(head, 2)) == \
        "<ListNode: [1 -> 2 -> 3 -> 5]>"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    func = Solution().removeNthFromEnd

    head = ListNode(1)
    assert func(head, 1) is None


def test_leetcode_example_3() -> None:
    """The fird example in the task."""
    func = Solution().removeNthFromEnd

    head = ListNode(1)
    head.next = ListNode(2)
    assert str(func(head, 1)) == "<ListNode: [1]>"


def test_remove_unavailable() -> None:
    func = Solution().removeNthFromEnd

    head = ListNode(1)
    head.next = ListNode(2)
    assert str(func(head, 2)) == "<ListNode: [2]>"

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    assert str(func(head, 3)) == "<ListNode: [2 -> 3]>"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design Linked List.

https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
Created on Mon Apr 22 08:36:06 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Node(object):
    """The element of linked list."""

    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Node | None = None


class MyLinkedList:
    """Answer for leetcode."""

    def __init__(self) -> None:
        self.head: Node | None = None
        self.size = 0

    def _getNode(self, index: int) -> Node:
        if not (0 <= index < self.size):
            raise ValueError('Index is invalid')

        current = self.head
        for i in range(index + 1):
            if i == index:
                break
            if current is None:
                raise ValueError('Size of list is invalid - no next node')
            current = current.next
        if current is None:
            raise ValueError('Size of list is invalid - no current node')
        return current

    def get(self, index: int) -> int:
        """
        Get the value of the indexth node in the linked list.

        If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        return self._getNode(index).val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element.

        After the insertion, the new node will be the first
        node of the linked list.
        """
        prev_head = self.head
        self.head = Node(val)
        self.head.next = prev_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """Append a node of value val as the last element."""
        if self.size == 0:
            self.addAtHead(val)
            return
        self._getNode(self.size-1).next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index'th node.

        If index equals the length of the linked list, the node
        will be appended to the end of the linked list.
        If index is greater than the length, the node
        will not be inserted.
        """
        if index > self.size or index < 0:
            return

        if index == self.size:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return

        current = self._getNode(index - 1)
        old = current.next
        current.next = Node(val)
        current.next.next = old
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """Delete the index'th node in the linked list.

        If the index is invalid - do nothing
        """
        if index >= self.size or index < 0:
            return

        self.size -= 1

        if index == 0:
            old = self.head
            if old is None:
                raise ValueError('Size of list is invalid - no old node')
            self.head = old.next
            del old
            return
        prev = self._getNode(index - 1)
        old = prev.next
        if old is None:
            raise ValueError('Size of list is invalid - no old.next node')
        prev.next = old.next
        del old

    def __repr__(self) -> str:
        """Representation of object is [head -> val -> tail]."""
        current = self.head
        result = ""
        while current is not None:
            if result:
                result += " -> "
            result += str(current.val)
            current = current.next
        return "[" + result + "]"


if __name__ == "__main__":
    obj = MyLinkedList()
    print(timer(obj.get)(0))
    timer(obj.addAtHead)(1)
    timer(obj.addAtTail)(3)
    timer(obj.addAtIndex)(1, 2)
    print(obj)
    timer(obj.deleteAtIndex)(0)
    print(obj)

#########
# Tests
# pylint: disable=missing-function-docstring


class TestMyLinkedList:
    """Test class."""

    @staticmethod
    def test_get() -> None:
        """My testcases."""
        c = MyLinkedList()

        assert c.get(-1) == -1

        assert c.get(0) == -1

        assert c.get(1) == -1

        c.addAtHead(2)

        assert c.get(-1) == -1

        assert c.get(0) == 2

        assert c.get(1) == -1

        c.addAtHead(1)

        assert c.get(0) == 1

        assert c.get(1) == 2

        assert c.get(3) == -1

    @staticmethod
    def test_addAtHead() -> None:
        """My testcases."""
        c = MyLinkedList()

        c.addAtHead(1)
        assert str(c) == "[1]"

        c.addAtHead(2)
        assert str(c) == "[2 -> 1]"

    @staticmethod
    def test_addAtTail() -> None:
        """My testcases."""
        c = MyLinkedList()

        c.addAtTail(1)
        assert str(c) == "[1]"

        c.addAtTail(2)
        assert str(c) == "[1 -> 2]"

    @staticmethod
    def test_addAtIndex() -> None:
        """My testcases."""
        c = MyLinkedList()

        c.addAtIndex(1, 1)
        assert str(c) == "[]"

        c.addAtIndex(-1, 1)
        assert str(c) == "[]"

        c.addAtIndex(0, 1)
        assert str(c) == "[1]"

        c.addAtIndex(-1, 2)
        assert str(c) == "[1]"

        c.addAtIndex(2, 2)
        assert str(c) == "[1]"

        c.addAtIndex(1, 2)
        assert str(c) == "[1 -> 2]"

        c.addAtIndex(0, 3)
        assert str(c) == "[3 -> 1 -> 2]"

        c.addAtIndex(1, 4)
        assert str(c) == "[3 -> 4 -> 1 -> 2]"

    @staticmethod
    def test_deleteAtIndex() -> None:
        """My testcases."""
        c = MyLinkedList()

        c.deleteAtIndex(0)
        assert str(c) == "[]"

        c.addAtTail(1)
        c.deleteAtIndex(0)
        assert str(c) == "[]"

        c.addAtTail(1)
        c.deleteAtIndex(1)
        assert str(c) == "[1]"

        c.addAtTail(2)
        c.deleteAtIndex(1)
        assert str(c) == "[1]"

        c.addAtTail(2)
        c.addAtTail(3)
        c.deleteAtIndex(1)
        assert str(c) == "[1 -> 3]"

        c.deleteAtIndex(0)
        assert str(c) == "[3]"


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    assert obj.get(1) == 2
    obj.deleteAtIndex(1)
    assert obj.get(1) == 3

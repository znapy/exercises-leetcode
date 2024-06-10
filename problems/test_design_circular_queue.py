#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design Circular Queue.

https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/
Created on Mon Jun 10 09:01:31 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class MyCircularQueue:
    """Leetcode class for answers."""

    def __init__(self, k: int):
        """Initialize the object with the size of the queue to be k."""
        self.queue: list[int] = [0] * k
        self.front = -1
        self.end = -1

    def enQueue(self,  # pylint: disable=invalid-name
                value: int) -> bool:
        """
        Insert an element into the circular queue.

        Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.end += 1
        if self.end == len(self.queue):
            self.end = 0

        self.queue[self.end] = value

        if self.front == -1:
            self.front = 0

        return True

    def deQueue(self  # pylint: disable=invalid-name
                ) -> bool:
        """
        Delete an element from the circular queue.

        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        if self.front == self.end:
            self.front = -1
            self.end = -1
            return True

        self.front += 1
        if self.front == len(self.queue):
            self.front = 0

        return True

    def Front(self  # pylint: disable=invalid-name
              ) -> int:
        """
        Get the front item from the queue.

        If the queue is empty, return -1.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self  # pylint: disable=invalid-name
             ) -> int:
        """
        Get the last item from the queue.

        If the queue is empty, return -1.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.end]

    def isEmpty(self  # pylint: disable=invalid-name
                ) -> bool:
        """Check whether the circular queue is empty or not."""
        return self.front == -1

    def isFull(self  # pylint: disable=invalid-name
               ) -> bool:
        """Check whether the circular queue is full or not."""
        if self.end == len(self.queue)-1:
            return self.front == 0
        return self.end + 1 == self.front


def main() -> None:
    """Start point."""
    q = MyCircularQueue(3)

    print("result:", timer(q.enQueue)(1))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


class TestMyCircularQueue:
    """Test class."""

    @staticmethod
    def test_enQueue(  # pylint: disable=invalid-name
            ) -> None:
        """Leetcode and my testcases."""
        q = MyCircularQueue(3)

        # Leetcode example 1
        assert q.enQueue(1) is True
        assert q.enQueue(2) is True
        assert q.enQueue(3) is True
        assert q.enQueue(4) is False
        assert q.Rear() == 3
        assert q.isFull() is True
        assert q.deQueue() is True
        assert q.enQueue(4) is True
        assert q.Rear() == 4

        # My
        assert q.Front() == 2
        assert q.isFull() is True
        assert q.deQueue() is True
        assert q.Front() == 3
        assert q.isFull() is False
        assert q.Rear() == 4
        assert q.enQueue(5) is True
        assert q.enQueue(6) is False
        assert q.isFull() is True
        assert q.isEmpty() is False
        assert q.deQueue() is True
        assert q.isFull() is False
        assert q.isEmpty() is False
        assert q.deQueue() is True
        assert q.isEmpty() is False
        assert q.deQueue() is True
        assert q.isFull() is False
        assert q.isEmpty() is True

        # Leetcode unittest 1
        q = MyCircularQueue(6)
        assert q.enQueue(6) is True
        assert q.Rear() == 6
        assert q.Rear() == 6
        assert q.deQueue() is True
        assert q.enQueue(5) is True
        assert q.Rear() == 5
        assert q.deQueue() is True
        assert q.Front() == -1
        assert q.deQueue() is False
        assert q.deQueue() is False
        assert q.deQueue() is False

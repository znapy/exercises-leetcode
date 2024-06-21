#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement Queue using Stacks.

https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1386/
Created on Fri Jun 21 09:45:56 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from timer import timer


class MyQueue:
    """Leetcode class for answers."""

    def __init__(self) -> None:
        self.income: deque[int] = deque()
        self.outcome: deque[int] = deque()

    def push(self, x: int) -> None:
        """Pushes element x to the back of the queue."""
        self.income.appendleft(x)

    def _rotate(self) -> None:
        "Fill outcome stack."
        if len(self.outcome):
            return
        while self.income:
            self.outcome.appendleft(self.income.popleft())

    def pop(self) -> int:
        "Removes the element from the front of the queue and returns it."
        self._rotate()
        if not len(self.outcome):
            raise ValueError("The queue is empty")
        return self.outcome.popleft()

    def peek(self) -> int:
        "Returns the element at the front of the queue."
        self._rotate()
        if not len(self.outcome):
            raise ValueError("The queue is empty")
        return self.outcome[0]

    def empty(self) -> bool:
        "Returns true if the queue is empty, false otherwise."
        self._rotate()
        return len(self.outcome) == 0


def main() -> None:
    """Start point."""
    myq = MyQueue()
    timed_push = timer(myq.push)
    timed_peek = timer(myq.peek)
    timed_pop = timer(myq.pop)
    timed_empty = timer(myq.empty)
    result: list[int | bool] = []
    timed_push(1)  # queue is: [1]
    timed_push(2)  # queue is: [1, 2] (leftmost is front of the queue)
    result.append(timed_peek())  # return 1
    result.append(timed_pop())  # return 1, queue is [2]
    result.append(timed_empty())  # return false
    print("result:", result)


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    myq = MyQueue()
    myq.push(1)
    myq.push(2)
    assert myq.peek() == 1
    assert myq.pop() == 1
    assert myq.empty() is False


def test_common() -> None:
    """The third example in the task."""
    myq = MyQueue()
    assert myq.empty() is True
    myq.push(1)
    assert myq.empty() is False
    assert myq.pop() == 1
    assert myq.empty() is True

    myq.push(2)
    myq.push(3)
    assert myq.pop() == 2
    myq.push(4)
    myq.push(5)
    assert myq.pop() == 3
    assert myq.peek() == 4

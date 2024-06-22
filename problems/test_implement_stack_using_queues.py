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


class MyStack:
    """Leetcode class for answers."""

    def __init__(self) -> None:
        self.queue: deque[int] = deque()

    def push(self, x: int) -> None:
        "Pushes element x to the top of the stack."
        self.queue.append(x)

    def pop(self) -> int:
        "Removes the element on the top of the stack and returns it."
        if not len(self.queue):
            raise ValueError("Queue is empty")
        tmp: deque[int] = deque()
        while True:
            last = self.queue.popleft()
            if not len(self.queue):
                self.queue = tmp
                return last
            tmp.append(last)

    def top(self) -> int:
        "Returns the element on the top of the stack."
        if not len(self.queue):
            raise ValueError("Queue is empty")
        tmp: deque[int] = deque()
        while True:
            last = self.queue.popleft()
            tmp.append(last)
            if not len(self.queue):
                self.queue = tmp
                return last

    def empty(self) -> bool:
        "Returns true if the stack is empty, false otherwise."
        return len(self.queue) == 0


def main() -> None:
    """Start point."""
    mys = MyStack()
    timed_push = timer(mys.push)
    timed_top = timer(mys.top)
    timed_pop = timer(mys.pop)
    timed_empty = timer(mys.empty)
    result: list[int | bool] = []
    timed_push(1)
    timed_push(2)
    result.append(timed_top())
    result.append(timed_pop())
    result.append(timed_empty())
    print("result:", result)


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    mys = MyStack()
    mys.push(1)
    mys.push(2)
    assert mys.top() == 2
    assert mys.pop() == 2
    assert mys.empty() is False


def test_common() -> None:
    """The third example in the task."""
    mys = MyStack()
    assert mys.empty() is True
    mys.push(1)
    assert mys.empty() is False
    assert mys.pop() == 1
    assert mys.empty() is True

    mys.push(2)
    mys.push(3)
    assert mys.pop() == 3
    mys.push(4)
    mys.push(5)
    assert mys.pop() == 5
    assert mys.top() == 4

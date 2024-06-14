#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Min Stack.

https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/
Created on Fri Jun 14 06:53:07 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class NodeMS:
    """Implementation for MinStack."""

    def __init__(self, val: int, head: ['NodeMS', None]):
        self.val, self.head = val, head


class MinStack:
    """Leetcode class for answers."""
    # Leetcode solution - keep minimum value for eache node
    #   and do not calculate it in every pop call.
    #   Or we can use double lists - one for current values
    #   and one for minimums.

    def __init__(self) -> None:
        self.min: int | None = None
        self.head: NodeMS | None = None
        self.vals: dict[int, int] = dict()

    def push(self, val: int) -> None:
        """Pushes the element val onto the stack."""
        self.head = NodeMS(val, self.head)

        self.vals[val] = self.vals.get(val, 0) + 1

        if self.min is None:
            self.min = val
        else:
            self.min = min(self.min, val)

    def pop(self) -> None:
        """Remove the element on the top of the stack."""
        if self.head is None:
            raise ValueError("MinStack is empty - we can't pop element")
        val = self.head.val
        self.head = self.head.head

        items = self.vals.get(val, 0) - 1
        if items == 0:
            del self.vals[val]
        else:
            self.vals[val] = items

        if self.vals:
            self.min = min(self.vals)
        else:
            self.min = None

    def top(self) -> int:
        """Get the top element of the stack."""
        if self.head is None:
            raise ValueError("MinStack is empty - we can't get a top element")
        return self.head.val

    def getMin(self  # pylint: disable=invalid-name
               ) -> int:
        """Retrieve the minimum element in the stack."""
        if self.min is None:
            raise ValueError("MinStack is empty - we can't get a top element")
        return self.min


def main() -> None:
    """Start point."""
    minStack = MinStack()
    timer(minStack.push)(-2)
    timer(minStack.push)(0)
    timer(minStack.push)(-3)
    timer(minStack.getMin)()
    timer(minStack.pop)()
    timer(minStack.top)()

    print("result:", timer(minStack.getMin)())


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2

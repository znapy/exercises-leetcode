#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fibonacci Number.

https://leetcode.com/explore/featured/card/recursion-i/255/recursion-memoization/1661/
Created on Thu May  9 08:50:34 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x: [int, 'ListNode'], next_: ["ListNode", None] = None
                 ) -> None:
        self.val = x
        self.next: ListNode | None = next_

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


class Solution:
    """Leetcode class for answers."""

    @staticmethod
    def fib_with_prev(counter: int, cur: int, prev: int) -> int:
        """Fibonachi in recursion."""
        if counter > 0:
            return Solution.fib_with_prev(counter - 1, cur + prev, cur)
        return cur + prev

    def fib(self,  # pylint: disable=invalid-name
            n: int) -> int:
        """Leetcode function as answer."""
        if n == 0:
            return 0
        if n == 1:
            return 1

        # fib(n-1) + fib(n-2)
        # - twice recursion, let's make it a little more efficient

        return Solution.fib_with_prev(n-2, 1, 0)


if __name__ == "__main__":
    func_timed = timer(Solution().fib)
    print("result:", func_timed(2))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    func = Solution().fib
    assert func(2) == 1


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    func = Solution().fib
    assert func(3) == 2


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    func = Solution().fib
    assert func(4) == 3


def test_5() -> None:
    assert Solution().fib(
        5) == 5


def test_6() -> None:
    assert Solution().fib(
        6) == 8


def test_7() -> None:
    assert Solution().fib(
        7) == 13

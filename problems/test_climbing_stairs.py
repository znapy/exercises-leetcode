#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Climbing Stairs.

https://leetcode.com/explore/featured/card/recursion-i/255/recursion-memoization/1662/
Created on Fri May 10 14:37:18 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from functools import lru_cache

from timer import timer


class Solution:
    """Leetcode class for answers."""

    @staticmethod
    def new_variants(row: list[int]) -> list[list[int]]:
        """Next variants of steps"""
        if row[-1] == 1:
            return [row + [1]] + [row[:-1] + [2]]
        # if prev[-1] == 2:
        return [row + [1]]

    @staticmethod
    def rows(counter: int, prev: list[list[int]]) -> list[list[int]]:
        """All variants of steps recursively."""
        if counter > 10:
            raise ValueError("Memory limit")
        if counter > 0:
            new_rows = []
            for row in prev:
                new_rows += Solution.new_variants(row)
            return Solution.rows(counter - 1, new_rows)
        return prev

    @lru_cache(maxsize=40, typed=True)
    @staticmethod
    def fib(n: int) -> int:
        """Fibonacci realization."""
        if n < 2:
            return n
        return Solution.fib(n-1) + Solution.fib(n-2)

    def climbStairs(self,  # pylint: disable=invalid-name
                    n: int) -> int:
        """Leetcode function as answer."""
        if n == 1:
            return 1

        # This is a fibonacci row for n+1, but lets calculate the combinations
        # - there is a memory error with a high value (f.e. 35)
        # return len(Solution.rows(n-1, [[1]]))

        # So answer will be with fibonacci
        return Solution.fib(n+1)


if __name__ == "__main__":
    func_timed = timer(Solution().climbStairs)
    print("result:", func_timed(34))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().climbStairs(
        2) == 2


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().climbStairs(
        3) == 3


def test_1() -> None:
    assert Solution().climbStairs(
        1) == 1


def test_4() -> None:
    assert Solution().climbStairs(
        4) == 5


def test_5() -> None:
    assert Solution().climbStairs(
        5) == 8


def test_6() -> None:
    assert Solution().climbStairs(
        6) == 13


def test_7() -> None:
    assert Solution().climbStairs(
        7) == 21


def test_8() -> None:
    assert Solution().climbStairs(
        8) == 34

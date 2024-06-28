#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sqrt(x).

https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
Created on Thu Jun 27 09:07:18 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def mySqrt(self,  # pylint: disable=invalid-name
               x: int) -> int:
        """Leetcode function as answer."""
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right


if __name__ == "__main__":
    func_timed = timer(Solution().mySqrt)
    print("result:", func_timed(9))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().mySqrt(
        4) == 2


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().mySqrt(
        8) == 2


def test_0() -> None:
    assert Solution().mySqrt(
        0) == 0


def test_1() -> None:
    assert Solution().mySqrt(
        1) == 1


def test_2() -> None:
    assert Solution().mySqrt(
        2) == 1


def test_3() -> None:
    assert Solution().mySqrt(
        3) == 1


def test_5() -> None:
    assert Solution().mySqrt(
        5) == 2


def test_9() -> None:
    assert Solution().mySqrt(
        9) == 3

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Height Checker.

https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/
Created on Mon Apr  1 09:56:04 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def heightChecker(self,  # pylint: disable=invalid-name
                      heights: list[int]) -> int:
        """Leetcode function as answer."""
        expected = sorted(heights)
        return sum([1 for i in range(len(heights))
                    if heights[i] != expected[i]])


if __name__ == "__main__":
    func_timed = timer(Solution().heightChecker)
    nums = [1, 1, 4, 2, 1, 3]
    print("result:", func_timed(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().heightChecker(
        [1, 1, 4, 2, 1, 3]) == 3


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().heightChecker(
        [5, 1, 2, 3, 4]) == 5


def test_leetcode_example_3() -> None:
    """The second example in the task."""
    assert Solution().heightChecker(
        [1, 2, 3, 4, 5]) == 0


def test_1() -> None:
    assert Solution().heightChecker(
        [1]) == 0


def test_1_2() -> None:
    assert Solution().heightChecker(
        [1, 2]) == 0


def test_2_1() -> None:
    assert Solution().heightChecker(
        [2, 1]) == 2


def test_2_2() -> None:
    assert Solution().heightChecker(
        [2, 2]) == 0


def test_1_2_1() -> None:
    assert Solution().heightChecker(
        [1, 2, 1]) == 2


def test_3_2_1() -> None:
    assert Solution().heightChecker(
        [3, 2, 1]) == 2


def test_3_1_2() -> None:
    assert Solution().heightChecker(
        [3, 1, 2]) == 3

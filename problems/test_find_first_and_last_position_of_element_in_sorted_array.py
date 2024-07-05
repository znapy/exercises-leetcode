#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Search for a Range.

https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/
Created on Wed Jul  3 07:53:20 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from bisect import bisect_left, bisect_right
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def searchRange(self,  # pylint: disable=invalid-name
                    nums: list[int], target: int) -> list[int]:
        """Leetcode function as answer."""
        left = bisect_left(nums, target)
        right = bisect_right(nums, target, left)
        if left == right:
            return [-1, -1]

        return [left, right-1]


if __name__ == "__main__":
    func_timed = timer(Solution().searchRange)
    print("result:", func_timed(list(range(10_000)), 0))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().searchRange(
        [5, 7, 7, 8, 8, 10], 8) == [3, 4]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().searchRange(
        [5, 7, 7, 8, 8, 10], target=6) == [-1, -1]


def test_leetcode_example_3() -> None:
    """The third     example in the task."""
    assert Solution().searchRange(
        [], target=0) == [-1, -1]

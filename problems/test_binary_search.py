#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Binary Search.

https://leetcode.com/explore/learn/card/binary-search/138/background/1038/
Created on Thu Jun 27 08:57:37 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def search(self, nums: list[int], target: int) -> int:
        """Leetcode function as answer."""
        left, right = 0, len(nums)-1
        while True:
            idx = left + (right-left)//2
            cur = nums[idx]
            if cur == target:
                return idx
            elif cur < target:
                left = idx + 1
            elif cur > target:
                right = idx - 1
            if right < left:
                return -1


if __name__ == "__main__":
    func_timed = timer(Solution().search)
    a, b = "11", "1"
    print("result:", func_timed([-1, 0, 3, 5, 9, 12], 2))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().search(
        [-1, 0, 3, 5, 9, 12], 9) == 4


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().search(
        [-1, 0, 3, 5, 9, 12], 2) == -1

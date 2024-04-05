#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Array and String: Find Pivot Index.

https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
Created on Thu Apr  4 09:44:22 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from itertools import accumulate
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def pivotIndex(self,  # pylint: disable=invalid-name
                   nums: list[int]) -> int:
        """Leetcode function as answer."""
        if len(nums) == 1:
            return 0

        sums_left_to_right = accumulate([0] + nums[:-1])
        sums_right_to_left = list(accumulate(nums[:0:-1]))[::-1] + [0]

        for i, val_lr in enumerate(sums_left_to_right):
            val_rl = sums_right_to_left[i]
            if val_lr == val_rl:
                return i
        return -1


if __name__ == "__main__":
    func_timed = timer(Solution().pivotIndex)
    nums = [1, 7, 3, 6, 5, 6]
    print("result:", func_timed(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().pivotIndex(
        [1, 7, 3, 6, 5, 6]) == 3


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().pivotIndex(
        [1, 2, 3]) == -1


def test_leetcode_check_1() -> None:
    """The second example in the task."""
    assert Solution().pivotIndex(
        [2, 1, -1]) == 0


def test_minus_1() -> None:
    assert Solution().pivotIndex(
        [-1]) == 0


def test_1() -> None:
    assert Solution().pivotIndex(
        [1]) == 0


def test_0() -> None:
    assert Solution().pivotIndex(
        [0]) == 0


def test_0_1() -> None:
    assert Solution().pivotIndex(
        [0, 1]) == 1


def test_1_0() -> None:
    assert Solution().pivotIndex(
        [1, 0]) == 0


def test_0_0() -> None:
    assert Solution().pivotIndex(
        [0, 0]) == 0


def test_1_1() -> None:
    assert Solution().pivotIndex(
        [1, 1]) == -1


def test_minus_1_1() -> None:
    assert Solution().pivotIndex(
        [-1, 1]) == -1


def test_1_minus_1() -> None:
    assert Solution().pivotIndex(
        [1, -1]) == -1


def test_0_0_0() -> None:
    assert Solution().pivotIndex(
        [0, 0, 0]) == 0


def test_1_0_0() -> None:
    assert Solution().pivotIndex(
        [1, 0, 0]) == 0


def test_0_1_0() -> None:
    assert Solution().pivotIndex(
        [0, 1, 0]) == 1


def test_0_0_1() -> None:
    assert Solution().pivotIndex(
        [0, 0, 1]) == 2


def test_1_0_1() -> None:
    assert Solution().pivotIndex(
        [1, 0, 1]) == 1


def test_1_1_1() -> None:
    assert Solution().pivotIndex(
        [1, 1, 1]) == 1


def test_1_minus_1_1() -> None:
    assert Solution().pivotIndex(
        [1, -1, 1]) == 0


def test_minuses_1_1_1() -> None:
    assert Solution().pivotIndex(
        [-1, -1, -1]) == 1


def test_0_minus_1_0() -> None:
    assert Solution().pivotIndex(
        [0, -1, 0]) == 1

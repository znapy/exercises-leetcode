#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Third Maximum Number.

https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
Created on Tue Apr  2 12:29:29 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    @timer
    def third_max_brute(self, nums: list[int]) -> int:
        """Third Maximum Number."""
        nums_sorted = sorted(nums, reverse=True)
        print(nums_sorted)
        if len(nums_sorted) < 3:
            return nums_sorted[0]
        first, second, third = None, None, None
        for val in nums_sorted:
            if first in (None, val):
                first = val
                continue
            if second in (None, val):
                second = val
                continue
            if third is None:
                third = val
            break
        if first is None:
            raise ValueError("The nums array is empty")
        if third is None:
            return first
        return third

    def thirdMax(self,  # pylint: disable=invalid-name
                 nums: list[int]) -> int:
        """Leetcode function as answer."""
        nums_sorted = sorted(set(nums), reverse=True)
        if len(nums_sorted) < 3:
            return nums_sorted[0]
        return nums_sorted[2]


if __name__ == "__main__":
    func_timed = timer(Solution().thirdMax)
    nums = [5, 1, 2, 3, 4]
    print("result:", func_timed(nums), Solution().third_max_brute(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().thirdMax(
        [3, 2, 1]) == 1


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().thirdMax(
        [1, 2]) == 2


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().thirdMax(
        [2, 2, 3, 1]) == 1


def test_0() -> None:
    assert Solution().thirdMax(
        [0]) == 0


def test_minuses_1_2() -> None:
    assert Solution().thirdMax(
        [-1, -2]) == -1


def test_0_0() -> None:
    assert Solution().thirdMax(
        [0, 0]) == 0


def test_0_0_0() -> None:
    assert Solution().thirdMax(
        [0, 0, 0]) == 0


def test_0_1_1() -> None:
    assert Solution().thirdMax(
        [0, 1, 1]) == 1


def test_0_0_1() -> None:
    assert Solution().thirdMax(
        [0, 0, 1]) == 1


def test_1_0_0() -> None:
    assert Solution().thirdMax(
        [1, 0, 0]) == 1


def test_0_1_0() -> None:
    assert Solution().thirdMax(
        [0, 1, 0]) == 1


def test_0_1_2() -> None:
    assert Solution().thirdMax(
        [0, 1, 2]) == 0


def test_0_1_2_3() -> None:
    assert Solution().thirdMax(
        [0, 1, 2, 3]) == 1


def test_3_2_1_0() -> None:
    assert Solution().thirdMax(
        [3, 2, 1, 0]) == 1

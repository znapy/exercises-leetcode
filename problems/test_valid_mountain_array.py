#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Valid Mountain Array.

https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
Created on Thu Mar 28 08:34:35 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def validMountainArray(self,  # pylint: disable=invalid-name
                           arr: list[int]) -> bool:
        """Leetcode function as answer."""
        length = len(arr)
        if length < 3:
            return False

        increase = False
        decrease = False
        for i in range(1, length):
            val_cur = arr[i]
            val_prev = arr[i-1]
            if val_prev == val_cur:
                return False
            if val_prev < val_cur:
                if decrease:
                    return False
                increase = True
                continue
            if not increase:
                return False
            decrease = True
        return increase and decrease


if __name__ == "__main__":
    func_timed = timer(Solution().validMountainArray)
    nums = [0, 2, 3, 3, 5, 2, 1, 0]
    print("result:", func_timed(nums))


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().validMountainArray(
        [2, 1]) is False


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().validMountainArray(
        [3, 5, 5]) is False


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().validMountainArray(
        [0, 3, 2, 1]) is True


def test_leetcode_check_1() -> None:
    assert Solution().validMountainArray(
        [0, 2, 3, 4, 5, 2, 1, 0]) is True


def test_leetcode_check_2() -> None:
    assert Solution().validMountainArray(
        [0, 2, 3, 3, 5, 2, 1, 0]) is False


def test_1() -> None:
    assert Solution().validMountainArray(
        [1]) is False


def test_1_2() -> None:
    assert Solution().validMountainArray(
        [1, 2]) is False


def test_2_1() -> None:
    assert Solution().validMountainArray(
        [2, 1]) is False


def test_1_2_0() -> None:
    assert Solution().validMountainArray(
        [1, 2, 0]) is True


def test_0_2_1() -> None:
    assert Solution().validMountainArray(
        [0, 2, 1]) is True


def test_2_0_1() -> None:
    assert Solution().validMountainArray(
        [2, 0, 1]) is False


def test_3_2_1() -> None:
    assert Solution().validMountainArray(
        [3, 2, 1]) is False


def test_1_2_1_0() -> None:
    assert Solution().validMountainArray(
        [1, 2, 1, 0]) is True


def test_0_1_2_1() -> None:
    assert Solution().validMountainArray(
        [0, 1, 2, 1]) is True


def test_1_2_1_2() -> None:
    assert Solution().validMountainArray(
        [1, 2, 1, 2]) is False


def test_1_2_1_2_1() -> None:
    assert Solution().validMountainArray(
        [1, 2, 1, 2, 1]) is False

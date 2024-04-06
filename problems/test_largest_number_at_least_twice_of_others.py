#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Largest Number At Least Twice of Others.

https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
Created on Sat Apr  6 09:18:32 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def dominantIndex(self,  # pylint: disable=invalid-name
                      nums: list[int]) -> int:
        """Leetcode function as answer."""
        s = sorted(nums)
        if s[-1] >= s[-2] * 2:
            return nums.index(s[-1])
        return -1


if __name__ == "__main__":
    func_timed = timer(Solution().dominantIndex)
    nums = [3, 6, 1, 0]
    print("result:", func_timed(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().dominantIndex(
        [3, 6, 1, 0]) == 1


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().dominantIndex(
        [1, 2, 3, 4]) == -1


def test_0_0() -> None:
    assert Solution().dominantIndex(
        [0, 0]) == 0


def test_1_0() -> None:
    assert Solution().dominantIndex(
        [1, 0]) == 0


def test_1_1() -> None:
    assert Solution().dominantIndex(
        [1, 1]) == -1


def test_1_2() -> None:
    assert Solution().dominantIndex(
        [1, 2]) == 1


def test_2_1() -> None:
    assert Solution().dominantIndex(
        [2, 1]) == 0


def test_2_2() -> None:
    assert Solution().dominantIndex(
        [2, 2]) == -1


def test_2_3() -> None:
    assert Solution().dominantIndex(
        [2, 3]) == -1


def test_3_2() -> None:
    assert Solution().dominantIndex(
        [3, 2]) == -1


def test_3_1() -> None:
    assert Solution().dominantIndex(
        [3, 1]) == 0


def test_1_3() -> None:
    assert Solution().dominantIndex(
        [1, 3]) == 1


def test_0_1_2() -> None:
    assert Solution().dominantIndex(
        [0, 1, 2]) == 2


def test_1_0_2() -> None:
    assert Solution().dominantIndex(
        [1, 0, 2]) == 2


def test_0_2_1() -> None:
    assert Solution().dominantIndex(
        [0, 2, 1]) == 1


def test_1_2_0() -> None:
    assert Solution().dominantIndex(
        [1, 2, 0]) == 1


def test_2_1_0() -> None:
    assert Solution().dominantIndex(
        [2, 1, 0]) == 0


def test_2_0_1() -> None:
    assert Solution().dominantIndex(
        [2, 0, 1]) == 0


def test_0_1_3() -> None:
    assert Solution().dominantIndex(
        [0, 1, 3]) == 2


def test_1_0_3() -> None:
    assert Solution().dominantIndex(
        [1, 0, 3]) == 2


def test_0_3_1() -> None:
    assert Solution().dominantIndex(
        [0, 3, 1]) == 1


def test_1_3_0() -> None:
    assert Solution().dominantIndex(
        [1, 3, 0]) == 1


def test_3_1_0() -> None:
    assert Solution().dominantIndex(
        [3, 1, 0]) == 0


def test_3_0_1() -> None:
    assert Solution().dominantIndex(
        [3, 0, 1]) == 0

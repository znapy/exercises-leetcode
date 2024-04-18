#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rotate Array.

https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1182/
Created on Wed Apr 17 08:39:54 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def rotate(self,  # pylint: disable=invalid-name
               nums: list[int], k: int) -> None:
        """
        Leetcode function as answer.

        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        nums[:] = nums[-k:] + nums[:len(nums) - k]


if __name__ == "__main__":
    func_timed = timer(Solution().rotate)
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    func_timed(nums, k)
    print("result:", nums)

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    nums = [-1, -100, 3, 99]
    Solution().rotate(nums, 2)
    assert nums == [3, 99, -1, -100]


def test_1_0() -> None:
    nums = [1]
    Solution().rotate(nums, 0)
    assert nums == [1]


def test_1_1() -> None:
    nums = [1]
    Solution().rotate(nums, 1)
    assert nums == [1]


def test_1_2_0() -> None:
    nums = [1, 2]
    Solution().rotate(nums, 0)
    assert nums == [1, 2]


def test_1_2_1() -> None:
    nums = [1, 2]
    Solution().rotate(nums, 1)
    assert nums == [2, 1]


def test_1_2_2() -> None:
    nums = [1, 2]
    Solution().rotate(nums, 2)
    assert nums == [1, 2]


def test_1_2_3() -> None:
    nums = [1, 2]
    Solution().rotate(nums, 3)
    assert nums == [2, 1]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Move Zeroes

https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
Created on Wed Mar 30 21:12:15 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def moveZeroes(self,  # pylint: disable=invalid-name
                   nums: list[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        writePointer = 0
        for i, val in enumerate(nums):
            if val != 0:
                if i != writePointer:
                    nums[writePointer] = val
                    nums[i] = 0
                writePointer += 1


if __name__ == "__main__":
    func_timed = timer(Solution().moveZeroes)
    nums = [0, 1, 0, 3, 12]
    print("result:", func_timed(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    nums = [0]
    Solution().moveZeroes(nums)
    assert nums == [0]


def test_1() -> None:
    nums = [1]
    Solution().moveZeroes(nums)
    assert nums == [1]


def test_minus_1_1() -> None:
    nums = [-1, 1]
    Solution().moveZeroes(nums)
    assert nums == [-1, 1]


def test_1_minus_1() -> None:
    nums = [1, -1]
    Solution().moveZeroes(nums)
    assert nums == [1, -1]


def test_1_0_1() -> None:
    nums = [1, 0, -1]
    Solution().moveZeroes(nums)
    assert nums == [1, -1, 0]


def test_0_0() -> None:
    nums = [0, 0]
    Solution().moveZeroes(nums)
    assert nums == [0, 0]


def test_0_0_0() -> None:
    nums = [0, 0, 0]
    Solution().moveZeroes(nums)
    assert nums == [0, 0, 0]


def test_1_0_0() -> None:
    nums = [1, 0, 0]
    Solution().moveZeroes(nums)
    assert nums == [1, 0, 0]


def test_0_0_1() -> None:
    nums = [0, 0, 1]
    Solution().moveZeroes(nums)
    assert nums == [1, 0, 0]


def test_minuses_1_2_3() -> None:
    nums = [-1, -2, -3]
    Solution().moveZeroes(nums)
    assert nums == [-1, -2, -3]

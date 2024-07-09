#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Two Sum II - Input array is sorted.

https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/
Created on Mon Apr 15 12:24:48 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def twoSum(self,  # pylint: disable=invalid-name
               numbers: list[int], target: int) -> list[int]:
        """Leetcode function as answer."""
        length = len(numbers)
        for left in range(length):
            remains = target - numbers[left]
            right_low, right_high = left + 1, length-1
            while right_low < right_high:
                right_mid = right_low + (right_high - right_low)//2
                if numbers[right_mid] < remains:
                    right_low = right_mid + 1
                else:
                    right_high = right_mid
            if numbers[right_low] == remains:
                break
        return [left + 1, right_low + 1]


if __name__ == "__main__":
    func_timed = timer(Solution().twoSum)
    numbers = [2, 7, 11, 15]
    target = 9
    print("result:", func_timed(numbers, target))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().twoSum(
        [2, 7, 11, 15], 9) == [1, 2]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().twoSum(
        [2, 3, 4], 6) == [1, 3]


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().twoSum(
        [-1, 0], -1) == [1, 2]


def test_common() -> None:
    func = Solution().twoSum
    assert func([0, 0], 0) == [1, 2]
    assert func([0, 0, 1], 0) == [1, 2]
    assert func([1, 1, 2], 2) == [1, 2]
    assert func([-1, -1, 0], -2) == [1, 2]
    assert func([1, 2, 3, 4, 5, 6], 3) == [1, 2]
    assert func([1, 2, 3, 4, 5, 6], 4) == [1, 3]
    assert func([1, 2, 2, 4, 5, 6], 5) == [1, 4]
    assert func([1, 2, 2, 3, 5, 6], 6) == [1, 5]
    assert func([1, 2, 2, 3, 3, 6], 7) == [1, 6]
    assert func([0]*499 + [2, 3] + [9]*499, 5) == [500, 501]

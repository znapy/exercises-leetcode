#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find Minimum in Rotated Sorted Array.

https://leetcode.com/explore/learn/card/binary-search/126/template-ii/949/
Created on Wed Jul  3 07:45:07 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def findMin(self,  # pylint: disable=invalid-name
                nums: list[int]) -> int:
        """Leetcode function as answer."""
        low, high, first = 0, len(nums)-1, nums[0]
        if nums[high] > nums[low]:  # no rotation
            return first

        while low < high:
            mid = low + (high-low)//2
            if nums[mid] < first:  # we are in tail
                high = mid
            else:
                low = mid+1

        return nums[low]


if __name__ == "__main__":
    func_timed = timer(Solution().findMin)
    a, b = "11", "1"
    print("result:", func_timed([4, 5, 6, 7, 0, 1, 2]))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().findMin(
        [3, 4, 5, 1, 2]) == 1


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().findMin(
        [4, 5, 6, 7, 0, 1, 2]) == 0


def test_leetcode_example_3() -> None:
    """The third     example in the task."""
    assert Solution().findMin(
        [11, 13, 15, 17]) == 11


def test_common() -> None:
    func = Solution().findMin
    assert func([0]) == 0
    assert func([-1]) == -1
    assert func([-1, 1]) == -1
    assert func([1, -1]) == -1
    assert func([0, 1, 2]) == 0
    assert func([1, 2, 0]) == 0
    assert func([2, 0, 1]) == 0
    assert func([1, 2, 3, 4]) == 1
    assert func([2, 3, 4, 1]) == 1
    assert func([3, 4, 1, 2]) == 1
    assert func([4, 1, 2, 3]) == 1

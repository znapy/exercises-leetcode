#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
First Bad Version.

https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/
Created on Sun Jun 30 10:23:05 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from math import inf
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def findPeakElement(self,  # pylint: disable=invalid-name
                        nums: list[int]) -> int:
        """Leetcode function as answer."""
        idx_l, idx_r, idx_max = 0, len(nums)-1, len(nums)-1
        while True:
            idx_m = idx_l + (idx_r - idx_l)//2
            if idx_l == idx_m:
                return idx_l if nums[idx_l] > nums[idx_r] else idx_r
            val_l = -inf if idx_m == 0 else nums[idx_m-1]
            val_r = -inf if idx_m == idx_max else nums[idx_m+1]
            greater_l, greater_r = nums[idx_m] > val_l, nums[idx_m] > val_r
            if greater_l and greater_r:
                return idx_m
            if greater_l:
                idx_l = idx_m
            else:
                idx_r = idx_m
        # Leetcode solution:
        # low, high = 0, len(nums)-1
        # while low < high:
        #     mid = low + int((high-low)/2)
        #     if nums[mid] < nums[mid+1]:
        #         low = mid+1
        #     else:
        #         high = mid
        # return low


if __name__ == "__main__":
    func_timed = timer(Solution().findPeakElement)
    print("result:", func_timed([1, 6, 5, 4, 3, 2, 1]))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().findPeakElement(
        [1, 2, 3, 1]) == 2


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().findPeakElement(
        [1, 2, 1, 3, 5, 6, 4]) == 5


def test_common() -> None:
    f = Solution().findPeakElement
    # my
    assert f([0]) == 0
    assert f([0, -1]) == 0
    assert f([-1, 0]) == 1

    assert f([0, 1, 2]) == 2
    assert f([0, 2, 1]) == 1

    assert f([1, 2, 0]) == 1
    assert f([1, 0, 2]) in [0, 2]

    assert f([2, 0, 1]) in [0, 2]
    assert f([2, 1, 0]) == 0

    # Leetcode unittest 1
    assert f([1, 6, 5, 4, 3, 2, 1]) == 1

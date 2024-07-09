#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find Minimum in Rotated Sorted Array II.

https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1031/
Created on Mon Jul  8 11:07:58 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer
from heapq import nsmallest


class Solution:
    """Leetcode class for answers."""

    def findMin(self,  # pylint: disable=invalid-name
                nums: list[int]) -> int:
        """Leetcode function as answer."""
        low, high, first = 0, len(nums)-1, nums[0]
        if nums[high] > nums[low]:  # no rotation
            return first

        def lower(left: int, right: int) -> int:
            for idx in range(left, right):
                if nums[idx] < first:
                    return idx
            return right

        while low < high:
            mid = low + (high-low)//2
            if nums[mid] < first:  # we are in the tail
                high = mid
                continue
            if nums[mid] > first:  # we are in the head
                low = mid+1
                continue
            # the middle is the same as the first - we need to check in a row
            low = lower(low, mid)
            if low == mid:
                low = mid+1
            else:
                high = mid

        return nums[low]


if __name__ == "__main__":
    func_timed = timer(Solution().findMin)
    nums = [1, 1, 1, 1, 1, 1, 0, 1, 1]
    print("result:", func_timed(nums))
    print("builtin 1:", timer(min)(nums))
    print("builtin 2:", timer(nsmallest)(1, nums)[0])

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().findMin(
        [1, 3, 5]) == 1


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().findMin(
        [2, 2, 2, 0, 1]) == 0


def test_common() -> None:
    func = Solution().findMin
    assert func([0]) == 0
    assert func([0, 0]) == 0
    assert func([0, 1, 1]) == 0
    assert func([0, 0, 1]) == 0
    assert func([0, 0, 1, 2]) == 0
    assert func([0, 0, 0, 1, 2]) == 0
    assert func([2, 0, 1]) == 0
    assert func([2, 0, 0, 1]) == 0
    assert func([2, 0, 0, 0, 1]) == 0
    assert func([1, 2, 0]) == 0
    assert func([1, 2, 0, 0]) == 0
    assert func([1, 2, 0, 0, 0]) == 0
    assert func([1, 0, 1, 1, 1]) == 0
    assert func([1, 1, 0, 1, 1]) == 0
    assert func([1, 1, 1, 0, 1]) == 0
    assert func([1, 0, 1, 1, 1, 1, 1]) == 0
    assert func([1, 1, 0, 1, 1, 1, 1]) == 0
    assert func([1, 1, 1, 1, 0, 1, 1]) == 0
    assert func([1, 1, 1, 1, 1, 0, 1]) == 0
    assert func([1, 1, 0, 1, 1, 1, 1, 1, 1]) == 0
    assert func([1, 1, 1, 1, 1, 1, 0, 1, 1]) == 0

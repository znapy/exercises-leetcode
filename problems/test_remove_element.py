#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Remove Element.

https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
Created on Mon Mar 25 10:15:04 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""


class Solution:
    """Leetcode class for answers."""

    def removeElement(self,  # pylint: disable=invalid-name
                      nums: list[int], val: int) -> int:
        """Leetcode function as answer."""
        length = len(nums)
        for i in range(length):
            if i == length:
                break
            if nums[i] == val:
                length -= 1
                while length > i:
                    if nums[length] != val:
                        break
                    length -= 1
                if i == length:
                    break
                nums[i] = nums[length]

        return length

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """Fhe first example in the task."""
    nums = [3, 2, 2, 3]
    val = 3
    result = Solution().removeElement(nums, val)
    assert result == 2
    assert nums[:result] == [2, 2]


def test_leetcode_example_2() -> None:
    """Fhe second example in the task."""
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    result = Solution().removeElement(nums, val)
    assert result == 5
    assert nums[:result] == [0, 1, 4, 0, 3]

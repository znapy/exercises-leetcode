#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Merge Sorted Array.

https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
Created on Wed Mar 24 17:19:35 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""


class Solution:
    """Leetcode class for answers."""

    def merge(self,  # pylint: disable=invalid-name
              nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Leetcode function as answer.

        Do not return anything, modify nums1 in-place instead.
        """
        result = nums1[:m] + nums2
        result = sorted(result)
        for i in range(m+n):
            nums1[i] = result[i]

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    nums1 = [1]
    m = 1
    nums2: list[int] = []
    n = 0
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1]


def test_leetcode_example_3() -> None:
    """The fird example in the task."""
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1]

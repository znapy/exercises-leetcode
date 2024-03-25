#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Merge Sorted Array.

https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
Created on Wed Mar 24 17:19:35 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    @timer
    def merge_brute(self,
                    nums1: list[int], m: int,
                    nums2: list[int], n: int) -> None:
        """Bruteforce."""
        nums1[:] = sorted(nums1[:m] + nums2)

    def merge(self,  # pylint: disable=invalid-name
              nums1: list[int], m: int,
              nums2: list[int], n: int) -> None:
        """
        Leetcode function as answer.

        Do not return anything, modify nums1 in-place instead.
        """
        result = nums1[:m] + nums2
        result = sorted(result)
        for i in range(m+n):
            nums1[i] = result[i]


if __name__ == "__main__":

    m = 197
    n = 3
    nums1 = [x for x in range(4, 201)] + [0, 0, 0]
    nums2 = [1, 2, 3]
    result = [x for x in range(1, 201)]

    merge_timed = timer(Solution().merge)
    merge_timed(nums1, m, nums2, n)
    assert nums1 == result

    nums1 = [x for x in range(4, 201)] + [0, 0, 0]
    Solution().merge_brute(nums1, m, nums2, n)  # built-in is faster :)
    assert nums1 == result

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


def test_empty() -> None:
    nums1: list[int] = []
    m = 0
    nums2: list[int] = []
    n = 0
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == []


def test_one_zero() -> None:
    nums1 = [0]
    m = 0
    nums2 = [0]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [0]


def test_two_zero() -> None:
    nums1 = [0, 0]
    m = 1
    nums2 = [0]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [0, 0]


def test_negative_and_zero() -> None:
    nums1 = [-1, 0]
    m = 1
    nums2 = [0]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [-1, 0]


def test_few_negatives() -> None:
    nums1 = [-2, -1, 0, 0]
    m = 2
    nums2 = [-4, -3]
    n = 2
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [-4, -3, -2, -1]

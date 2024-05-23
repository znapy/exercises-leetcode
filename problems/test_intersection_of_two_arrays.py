#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intersection of Two Arrays.

https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/
Created on Wed May 22 08:39:25 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def intersection(self,  # pylint: disable=invalid-name
                     nums1: list[int], nums2: list[int]) -> list[int]:
        """Leetcode function as answer."""
        return list(set(nums1) & set(nums2))


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().intersection)
    nums1 = list(range(1000))
    nums2 = list(range(999))
    print("result:", func_timed(nums1, nums2))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().intersection(
        [1, 2, 2, 1], [2, 2]) == [2]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().intersection(
        [4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]

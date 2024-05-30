#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intersection of Two Arrays II.

https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1178/
Created on Wed May 29 08:55:05 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import Counter

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def intersect(self,  # pylint: disable=invalid-name
                  nums1: list[int], nums2: list[int]) -> list[int]:
        """Leetcode function as answer."""
        return list(
            (Counter(nums1) & Counter(nums2))
            .elements())


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().intersect)
    print("result:", func_timed(
        ["a"]*998 + ["b"]*2,
        ["a"] + ["b"]*998 + ["c"]))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().intersect(
        [1, 2, 2, 1], [2, 2]) == [2, 2]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert sorted(Solution().intersect(
        [4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]

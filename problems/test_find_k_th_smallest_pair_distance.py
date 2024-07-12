#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find K-th Smallest Pair Distance.

https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1041/
Created on Thu Jul 11 13:03:44 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from bisect import bisect_left
from collections import defaultdict
import random
from timer import timer


class Solution:
    """Leetcode class for answers."""

    @staticmethod
    def brute(nums: list[int], k: int) -> int:
        """Brute force."""
        if len(nums) > 1000:
            raise ValueError("Brute calculations are too long")
        distances: defaultdict[int, int] = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                distances[abs(nums[i] - nums[j])] += 1

        for key in sorted(distances.keys()):
            k -= distances[key]
            if k <= 0:
                return key
        return -1

    @staticmethod
    def _pairs_in_distance(nums: list[int], distance: int) -> int:
        return -1

    def smallestDistancePair(self,  # pylint: disable=invalid-name
                             nums: list[int], k: int) -> int:
        """Leetcode function as answer."""
        dists_sorted = sorted(nums)
        return -1


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().smallestDistancePair)
    n = 1000
    nums = list(range(n))
    random.shuffle(nums)
    k = int(n * (n - 1) / 2)
    print("result brute:", timer(Solution.brute)(nums, k))
    print("result smallestDistancePair:", func_timed(nums, k))

    # nums = [1000, 1001, 998, 1004, 994, 1005, 988, 1012, 980, 1021, 970, 1032,
    #         958, 1045, 944, 1060]
    # nums2 = sorted(nums)
    # dists = {abs(nums2[i] - nums2[i-1]):
    #          (i-1, i) for i in range(1, len(nums2))}


if __name__ == "__main__":
    main()

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().brute(
        nums=[1, 3, 1], k=1) == 0


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().brute(
        nums=[1, 1, 1], k=2) == 0


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().brute(
        nums=[1, 6, 1], k=3) == 5


def test_common() -> None:
    func = Solution().brute

    assert func([0, 0], 1) == 0
    assert func([0, 0, 0], 1) == 0
    assert func([0, 0, 0], 2) == 0
    assert func([0, 0, 0], 3) == 0
    assert func([0, 0, 0, 0], 1) == 0
    assert func([0, 0, 0, 0], 2) == 0
    assert func([0, 0, 0, 0], 3) == 0
    assert func([0, 0, 0, 0], 4) == 0
    assert func([0, 0, 0, 0], 5) == 0
    assert func([0, 0, 0, 0], 6) == 0

    nums = [1000, 1001, 998, 1004, 994, 1005, 988, 1012, 980, 1021, 970, 1032,
            958, 1045, 944, 1060]
    random.shuffle(nums)  # the correct algoritm doesn't care about the order
    assert func(nums, 1) == 1
    assert func(nums, 120) == 116

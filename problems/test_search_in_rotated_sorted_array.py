#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Search in Rotated Sorted Array.

https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/
Created on Sat Jun 29 08:43:53 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def search(self, nums: list[int], target: int) -> int:
        """Leetcode function as answer."""
        left, right, first = 0, len(nums)-1, nums[0]
        in_head = target >= first
        in_tail = not in_head

        while True:
            idx = left + (right-left)//2
            cur = nums[idx]
            is_head, bigger = (cur >= first), (cur > target)
            is_tail, lower = not is_head, not bigger

            if cur == target:
                return idx

            if is_head and in_head and lower:
                left = idx + 1
            elif is_head and in_head and bigger:
                right = idx - 1
            elif is_head and in_tail:
                left = idx + 1
            elif is_tail and in_tail and lower:
                left = idx + 1
            elif is_tail and in_tail and bigger:
                right = idx - 1
            elif is_tail and in_head:
                right = idx - 1

            if right < left:
                return -1


if __name__ == "__main__":
    func_timed = timer(Solution().search)
    print("result:", func_timed([4, 5, 6, 7, 0, 1, 2], 0))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().search(
        [4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().search(
        [4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().search(
        [1], 0) == -1


def test_common() -> None:
    f = Solution().search
    assert f([1], 1) == 0
    assert f([1, 0], 1) == 0
    assert f([1, 0], 0) == 1
    assert f([0, 1], 0) == 0
    assert f([0, 1], 1) == 1
    assert f([-1, 1], 1) == 1
    assert f([1, -1], 1) == 0
    assert f([1, 2, 3], 1) == 0
    assert f([1, 2, 3], 2) == 1
    assert f([1, 2, 3], 3) == 2
    assert f([3, 1, 2], 3) == 0
    assert f([3, 1, 2], 1) == 1
    assert f([3, 1, 2], 2) == 2
    assert f([2, 3, 1], 1) == 2
    assert f([2, 3, 1], 2) == 0
    assert f([2, 3, 1], 3) == 1

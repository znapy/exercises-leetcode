#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Find All Numbers Disappeared in an Array.

https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
Created on Tue Apr  2 12:54:51 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def findDisappearedNumbers(self,  # pylint: disable=invalid-name
                               nums: list[int]) -> list[int]:
        """Leetcode function as answer."""
        nums_uniq = set(nums)
        return list(filter(lambda x: x not in nums_uniq,
                           range(1, len(nums)+1)))


if __name__ == "__main__":
    func_timed = timer(Solution().findDisappearedNumbers)
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print("result:", func_timed(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().findDisappearedNumbers(
        [4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().findDisappearedNumbers(
        [1, 1]) == [2]

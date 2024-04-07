#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plus One.

https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/
Created on Sat Apr  6 09:35:31 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def plusOne(self,  # pylint: disable=invalid-name
                digits: list[int]) -> list[int]:
        """Leetcode function as answer."""
        for i in range(1, len(digits) + 1):
            cur = digits[-i] + 1
            if cur < 10:
                digits[-i] = cur
                return digits
            digits[-i] = 0
        digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    func_timed = timer(Solution().plusOne)
    nums = [1, 2, 3]
    print("result:", func_timed(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().plusOne(
        [1, 2, 3]) == [1, 2, 4]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().plusOne(
        [4, 3, 2, 1]) == [4, 3, 2, 2]


def test_leetcode_example_3() -> None:
    """The second example in the task."""
    assert Solution().plusOne(
        [9]) == [1, 0]

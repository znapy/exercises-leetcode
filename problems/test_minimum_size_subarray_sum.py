#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimum Size Subarray Sum.

https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/
Created on Tue Apr 16 14:56:09 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def minSubArrayLen(self,  # pylint: disable=invalid-name
                       target: int, nums: list[int]) -> int:
        """Leetcode function as answer."""
        left, right, cur, top = -1, -1, 0, 100001  # max is 100000
        while True:
            right += 1
            if right == len(nums):
                break

            cur += nums[right]
            while cur >= target:
                top = min(top, right - left)

                if top == 1:
                    return 1

                left += 1
                cur -= nums[left]

        if top == 100001:
            return 0

        return top


if __name__ == "__main__":
    func_timed = timer(Solution().minSubArrayLen)
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print("result:", func_timed(target, nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().minSubArrayLen(
        7, [2, 3, 1, 2, 4, 3]) == 2


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().minSubArrayLen(
        4, [1, 4, 4]) == 1


def test_leetcode_example_3() -> None:
    """The second example in the task."""
    assert Solution().minSubArrayLen(
        11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0


def test_1_1() -> None:
    assert Solution().minSubArrayLen(
        1, [1]) == 1


def test_1_2() -> None:
    assert Solution().minSubArrayLen(
        1, [2]) == 1


def test_2_1() -> None:
    assert Solution().minSubArrayLen(
        2, [1]) == 0


def test_1_1_1() -> None:
    assert Solution().minSubArrayLen(
        1, [1, 1]) == 1


def test_2_1_1() -> None:
    assert Solution().minSubArrayLen(
        2, [1, 1]) == 2


def test_3_1_1() -> None:
    assert Solution().minSubArrayLen(
        3, [1, 1]) == 0


def test_3_1_2() -> None:
    assert Solution().minSubArrayLen(
        3, [1, 2]) == 2


def test_3_2_1() -> None:
    assert Solution().minSubArrayLen(
        3, [2, 1]) == 2


def test_1_2_3() -> None:
    assert Solution().minSubArrayLen(
        1, [2, 3]) == 1


def test_1000000000_x5() -> None:
    assert Solution().minSubArrayLen(
        1000000000, [10000]*100000) == 100000

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Sort Array By Parity.

https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
Created on Wed Mar 21 08:20:41 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    @timer
    def sort_array_by_parity_brute(self, nums: list[int]) -> list[int]:
        """Leetcode unswer."""
        nums[:] = [x for x in nums if x % 2 == 0] +\
                  [x for x in nums if x % 2 == 1]
        return nums

    def sortArrayByParity(self,  # pylint: disable=invalid-name
                          nums: list[int]) -> list[int]:
        """Leetcode function as answer."""
        if len(nums) == 1:
            return nums

        odd = len(nums) - 1
        even = 0
        while True:

            while even <= odd and nums[even] % 2 == 0:
                even += 1
            while even <= odd and nums[odd] % 2:
                odd -= 1
            if even > odd:
                break

            nums[even], nums[odd] = nums[odd], nums[even]

        return nums


if __name__ == "__main__":
    func_timed = timer(Solution().sortArrayByParity)
    nums = [3, 1, 2, 4]
    print("result:", func_timed(nums))
    print("result brute:", Solution().sort_array_by_parity_brute(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().sortArrayByParity(
        [3, 1, 2, 4]) == [4, 2, 1, 3]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().sortArrayByParity(
        [0]) == [0]


def test_1() -> None:
    assert Solution().sortArrayByParity(
        [1]) == [1]


def test_2() -> None:
    assert Solution().sortArrayByParity(
        [2]) == [2]


def test_1_0() -> None:
    assert Solution().sortArrayByParity(
        [1, 0]) == [0, 1]


def test_0_1() -> None:
    assert Solution().sortArrayByParity(
        [0, 1]) == [0, 1]


def test_0_2() -> None:
    assert Solution().sortArrayByParity(
        [0, 2]) == [0, 2]


def test_1_3() -> None:
    assert Solution().sortArrayByParity(
        [1, 3]) == [1, 3]


def test_0_0() -> None:
    assert Solution().sortArrayByParity(
        [0, 0]) == [0, 0]


def test_1_2_3() -> None:
    assert Solution().sortArrayByParity(
        [1, 2, 3]) == [2, 1, 3]


def test_2_3_4() -> None:
    assert Solution().sortArrayByParity(
        [2, 3, 4]) == [2, 4, 3]

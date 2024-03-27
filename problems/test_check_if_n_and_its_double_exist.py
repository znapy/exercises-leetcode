#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Check If N and Its Double Exist.

https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
Created on Wed Mar 27 08:21:45 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def checkIfExist(self,  # pylint: disable=invalid-name
                     arr: list[int]) -> bool:
        """
        Check If N and Its Double Exist.

        https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
        """
        arr2 = sorted(arr)
        for x in arr:
            quantity = arr2.count(x*2)
            if x == 0:
                if quantity > 1:
                    return True
                continue
            if quantity:
                return True
        return False


if __name__ == "__main__":
    func_timed = timer(Solution().checkIfExist)
    nums = [10, 2, 5, 3]  # [-4, -1, 0, 3, 10]  # [-2, -1, 0, 3, 4]
    print("result:", func_timed(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().checkIfExist(
        [10, 2, 5, 3]) is True


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().checkIfExist(
        [3, 1, 7, 11]) is False


def test_leetcode_check_1() -> None:
    """The second example in the task."""
    assert Solution().checkIfExist(
        [-2, 0, 10, -19, 4, 6, -8]) is False


def test_0_0() -> None:
    assert Solution().checkIfExist(
        [0, 0]) is True


def test_0_1() -> None:
    assert Solution().checkIfExist(
        [0, 1]) is False


def test_1_1() -> None:
    assert Solution().checkIfExist(
        [1, 1]) is False


def test_2_1() -> None:
    assert Solution().checkIfExist(
        [2, 1]) is True


def test_minus_1_0() -> None:
    assert Solution().checkIfExist(
        [-1, 0]) is False


def test_minus_1_minus_1() -> None:
    assert Solution().checkIfExist(
        [-1, -1]) is False


def test_minus_1_minus_2() -> None:
    assert Solution().checkIfExist(
        [-1, -2]) is True


def test_minus_2_minus_1() -> None:
    assert Solution().checkIfExist(
        [-2, -1]) is True


def test_1_2_3() -> None:
    assert Solution().checkIfExist(
        [1, 2, 3]) is True


def test_1_3_2() -> None:
    assert Solution().checkIfExist(
        [1, 3, 2]) is True


def test_2_4_8() -> None:
    assert Solution().checkIfExist(
        [2, 4, 8]) is True

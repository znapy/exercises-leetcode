#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Replace Elements with Greatest Element on Right Side.

https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
Created on Fri Mar 29 08:55:35 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def replaceElements(self,  # pylint: disable=invalid-name
                        arr: list[int]) -> list[int]:
        """Leetcode function as answer."""
        start = len(arr) - 1
        cur_max = 0
        for i in range(start, -1, -1):
            val = arr[i]
            if i == start:
                arr[i] = -1
                cur_max = val
                continue
            arr[i] = cur_max
            cur_max = max(cur_max, val)

        return arr

    @timer
    def replaceElements_notInPlace(self, arr: list[int]) -> list[int]:
        """
        Replace Elements with Greatest Element on Right Side - not in-place.
        """
        result: list[int] = []

        start = len(arr) - 1
        cur_max = 0
        for i in range(start, -1, -1):
            val = arr[i]
            if i == start:
                result.append(-1)
                cur_max = val
                continue
            result.insert(0, cur_max)
            cur_max = max(cur_max, val)

        return result


if __name__ == "__main__":
    s = Solution()
    func_timed = timer(s.replaceElements)

    # Why first execute is always longer?
    func_timed([17, 18, 5, 4, 6, 1])
    s.replaceElements_notInPlace([17, 18, 5, 4, 6, 1])

    s.replaceElements_notInPlace([i for i in range(10000)])
    func_timed([i for i in range(10000)])

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().replaceElements(
        [17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    arr = [0]
    res = Solution().replaceElements(arr)
    assert res == [-1]
    assert res is arr
    assert res == [-1]
    assert res is not [-1]  # another object with different id()


def test_0_1() -> None:
    assert Solution().replaceElements(
        [0, 1]) == [1, -1]


def test_1_0() -> None:
    assert Solution().replaceElements(
        [1, 0]) == [0, -1]


def test_1_2_3() -> None:
    assert Solution().replaceElements(
        [1, 2, 3]) == [3, 3, -1]


def test_3_2_1() -> None:
    assert Solution().replaceElements(
        [3, 2, 1]) == [2, 1, -1]


def test_2_3_1() -> None:
    assert Solution().replaceElements(
        [2, 3, 1]) == [3, 1, -1]


def test_1_3_2() -> None:
    assert Solution().replaceElements(
        [1, 3, 2]) == [3, 2, -1]

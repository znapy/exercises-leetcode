#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Duplicate Zeros.

https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
Created on Wed Mar 23 11:08:30 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""


class Solution:
    """Leetcode class for answers."""

    def duplicateZeros(self,  # pylint: disable=invalid-name
                       arr: list[int]) -> None:
        """
        Leetcode function as answer.

        Do not return anything, modify arr in-place instead.
        """
        queue: list[int] = []
        j = 0
        for i in range(len(arr)):
            num = arr[i]
            length_queue = len(queue) - j
            if length_queue or num == 0:
                queue.append(num)
            if length_queue and num == 0:
                queue.append(num)
            if length_queue:
                num = queue[j]
                j += 1
                arr[i] = num

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """Fhe first example in the task."""
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution().duplicateZeros(arr)
    assert arr == [1, 0, 0, 2, 3, 0, 0, 4]


def test_leetcode_example_2() -> None:
    """Fhe second example in the task."""
    arr = [1, 2, 3]
    Solution().duplicateZeros(arr)
    assert arr == [1, 2, 3]


def test_one_element_is_0() -> None:
    """Test extreme values 1."""
    arr = [0]
    Solution().duplicateZeros(arr)
    assert arr == [0]


def test_one_element_is_1() -> None:
    """Test extreme values 2."""
    arr = [1]
    Solution().duplicateZeros(arr)
    assert arr == [1]


def test_maximum_elements_with_1() -> None:
    """Test extreme values 3."""
    arr = [1]*9999
    Solution().duplicateZeros(arr)
    assert arr == [1]*9999


def test_maximum_elements_with_0() -> None:
    """Test extreme values 4."""
    arr = [0]*9999
    Solution().duplicateZeros(arr)
    assert arr == [0]*9999


def test_two_elements_01() -> None:
    arr = [0, 1]
    Solution().duplicateZeros(arr)
    assert arr == [0, 0]


def test_two_elements_10() -> None:
    arr = [1, 0]
    Solution().duplicateZeros(arr)
    assert arr == [1, 0]


def test_internal() -> None:
    arr = [1, 2, 0, 3, 4]
    Solution().duplicateZeros(arr)
    assert arr == [1, 2, 0, 0, 3]


def test_left() -> None:
    arr = [0, 1, 2]
    Solution().duplicateZeros(arr)
    assert arr == [0, 0, 1]


def test_right() -> None:
    arr = [1, 2, 0]
    Solution().duplicateZeros(arr)
    assert arr == [1, 2, 0]


def test_double_zero() -> None:
    arr = [0, 0, 1, 2, 3]
    Solution().duplicateZeros(arr)
    assert arr == [0, 0, 0, 0, 1]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Find Numbers with Even Number of Digits.

https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
Created on Wed Mar 21 16:36:01 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""


class Solution:
    """Leetcode class for answers."""

    def findNumbers(self,  # pylint: disable=invalid-name
                    nums: list[int]) -> int:
        """Leetcode function as answer."""
        answer = 0

        for num in nums:
            length = len(str(num))
            if length % 2 == 0:
                answer += 1

        return answer

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """Fhe first example in the task."""
    assert Solution().findNumbers(
        [12, 345, 2, 6, 7896]) == 2


def test_leetcode_example_2() -> None:
    """Fhe second example in the task."""
    assert Solution().findNumbers(
        [555, 901, 482, 1771]) == 1


def test_one_element_is_1() -> None:
    """Test extreme values 1."""
    assert Solution().findNumbers(
        [1]) == 0


def test_one_element_is_11() -> None:
    """Test extreme values 2."""
    assert Solution().findNumbers(
        [11]) == 1


def test_maximum_elements_with_1() -> None:
    """Test extreme values 3."""
    assert Solution().findNumbers(
        [1]*500) == 0


def test_maximum_elements_with_11() -> None:
    """Test extreme values 4."""
    assert Solution().findNumbers(
        [11]*500) == 500


def test_maximum_elements_odd() -> None:
    """Test extreme values 5."""
    assert Solution().findNumbers(
        [99999]*500) == 0


def test_maximum_elements_even() -> None:
    """Test extreme values 6."""
    assert Solution().findNumbers(
        [9999]*500) == 500


def test_internal() -> None:
    assert Solution().findNumbers(
        [1, 11, 11, 11, 1]) == 3


def test_left() -> None:
    assert Solution().findNumbers(
        [11, 11, 1]) == 2


def test_right() -> None:
    assert Solution().findNumbers(
        [1, 11, 11]) == 2


def test_corners() -> None:
    assert Solution().findNumbers(
        [11, 11, 1, 11, 11]) == 4

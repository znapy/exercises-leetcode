#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Max Consecutive Ones.

https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
Created on Wed Mar 20 09:17:04 2024
@author: znapy
"""


class Solution:
    """Leetcode class for answers."""

    def findMaxConsecutiveOnes(self,  # pylint: disable=invalid-name
                               nums: list[int]) -> int:
        """Leetcode function as answer."""
        answer = 0
        cur_sequence = 0
        prev = None

        for num in nums:
            if num == 1 and prev != 1:
                cur_sequence = 1
            if num == 1 and prev == 1:
                cur_sequence = cur_sequence + 1
            answer = max(answer, cur_sequence)
            prev = num

        return answer

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """Fhe first example in the task."""
    assert Solution().findMaxConsecutiveOnes(
        [1, 1, 0, 1, 1, 1]) == 3


def test_leetcode_example_2() -> None:
    """Fhe second example in the task."""
    assert Solution().findMaxConsecutiveOnes(
        [1, 0, 1, 1, 0, 1]) == 2


def test_one_element_is_0() -> None:
    """Test extreme values 1."""
    assert Solution().findMaxConsecutiveOnes(
        [0]) == 0


def test_one_element_is_1() -> None:
    """Test extreme values 2."""
    assert Solution().findMaxConsecutiveOnes(
        [1]) == 1


def test_maximum_elements_with_1() -> None:
    """Test extreme values 3."""
    assert Solution().findMaxConsecutiveOnes(
        [1]*100_000) == 100_000


def test_maximum_elements_with_0() -> None:
    """Test extreme values 4."""
    assert Solution().findMaxConsecutiveOnes(
        [0]*100_000) == 0


def test_two_elements_0() -> None:
    assert Solution().findMaxConsecutiveOnes(
        [0, 0]) == 0


def test_two_elements_1() -> None:
    assert Solution().findMaxConsecutiveOnes(
        [1, 1]) == 2


def test_internal() -> None:
    assert Solution().findMaxConsecutiveOnes(
        [0, 1, 1, 1, 0]) == 3


def test_left() -> None:
    assert Solution().findMaxConsecutiveOnes(
        [1, 1, 0, 1]) == 2


def test_right() -> None:
    assert Solution().findMaxConsecutiveOnes(
        [1, 0, 1, 1]) == 2


def test_similar() -> None:
    assert Solution().findMaxConsecutiveOnes(
        [1, 1, 0, 1, 1]) == 2

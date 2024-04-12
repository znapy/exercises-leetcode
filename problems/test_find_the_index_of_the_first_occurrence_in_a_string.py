#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement strStr().

https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/
Created on Thu Apr 11 08:56:09 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def strStr(self,  # pylint: disable=invalid-name
               haystack: str, needle: str) -> int:
        """Leetcode function as answer."""
        return haystack.find(needle)


if __name__ == "__main__":
    func_timed = timer(Solution().strStr)
    print("result:", func_timed("leetcode", "leeto"))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().strStr(
        "sadbutsad", "sad") == 0


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().strStr(
        "leetcode", "leeto") == -1


def test_a_a() -> None:
    assert Solution().strStr(
        "a", "a") == 0


def test_aa_a() -> None:
    assert Solution().strStr(
        "aa", "a") == 0


def test_a_aa() -> None:
    assert Solution().strStr(
        "a", "aa") == -1

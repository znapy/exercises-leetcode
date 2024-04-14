#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverse String.

https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/
Created on Sat Apr 13 21:11:28 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def reverseString(self,  # pylint: disable=invalid-name
                      s: list[str]) -> None:
        """
        Leetcode function as answer.

        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while j > i:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        # Simpliest solution without pointers: s[:] = s[::-1]


if __name__ == "__main__":
    func_timed = timer(Solution().reverseString)
    string = ["h", "e", "l", "l", "o"]
    func_timed(string)
    print("result:", string)

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    string = ["h", "e", "l", "l", "o"]
    Solution().reverseString(string)
    assert string == ['o', 'l', 'l', 'e', 'h']


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    string = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(string)
    assert string == ["h", "a", "n", "n", "a", "H"]


def test_a() -> None:
    string = ["a"]
    Solution().reverseString(string)
    assert string == ["a"]


def test_a_a() -> None:
    string = ["a", "a"]
    Solution().reverseString(string)
    assert string == ["a", "a"]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverse Words in a String III.

https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/
Created on Sat Apr 20 12:24:55 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def reverseWords(self,  # pylint: disable=invalid-name
                     s: str) -> str:
        """Leetcode function as answer."""
        result = " ".join(
                    map("".join,
                        map(reversed,
                            s.split())))
        return result


if __name__ == "__main__":
    func_timed = timer(Solution().reverseWords)
    print("result:", func_timed("Let's take LeetCode contest"))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().reverseWords(
        "Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().reverseWords(
        "Mr Ding") == "rM gniD"


def test_a() -> None:
    assert Solution().reverseWords(
        "a") == "a"


def test_aa() -> None:
    assert Solution().reverseWords(
        "aa") == "aa"


def test_ab() -> None:
    assert Solution().reverseWords(
        "ab") == "ba"

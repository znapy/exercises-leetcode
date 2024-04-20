#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverse Words in a String.

https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/
Created on Fri Apr 19 10:43:18 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def reverseWords(self,  # pylint: disable=invalid-name
                     s: str) -> str:
        """Leetcode function as answer."""
        result = " ".join(reversed(s.split()))
        return result
        # Also, checked nonbreaking space


if __name__ == "__main__":
    func_timed = timer(Solution().reverseWords)
    print("result:", func_timed("the sky is blue"))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().reverseWords(
        "the sky is blue") == "blue is sky the"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().reverseWords(
        "  hello world  ") == "world hello"


def test_leetcode_example_3() -> None:
    """The second example in the task."""
    assert Solution().reverseWords(
        "a good   example") == "example good a"


def test_a() -> None:
    assert Solution().reverseWords(
        "a") == "a"


def test__a_() -> None:
    assert Solution().reverseWords(
        "  a  ") == "a"


def test_with_nonbreaking_space() -> None:
    assert Solution().reverseWords(
        "a b") == "b a"

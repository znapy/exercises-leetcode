#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Longest Common Prefix.

https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/
Created on Fri Apr 12 08:19:41 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def longestCommonPrefix(self,  # pylint: disable=invalid-name
                            strs: list[str]) -> str:
        """Leetcode function as answer."""
        if len(strs) == 1:
            return strs[0]

        result: list[str] = []
        i, shortest, first = 0, len(strs[0]), True

        while i < shortest:
            etalon = strs[0]
            for val in strs[1:]:
                if first:
                    shortest = min(shortest, len(val))
                if i == shortest or val[i] != etalon[i]:

                    return "".join(result)

            result.append(etalon[i])
            i = i + 1
            first = False

        return "".join(result)


if __name__ == "__main__":
    func_timed = timer(Solution().longestCommonPrefix)
    print("result:", func_timed(["flower", "flow", "flight"]))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().longestCommonPrefix(
        ["flower", "flow", "flight"]) == "fl"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().longestCommonPrefix(
        ["dog", "racecar", "car"]) == ""


def test_() -> None:
    assert Solution().longestCommonPrefix(
        [""]) == ""


def test_a() -> None:
    assert Solution().longestCommonPrefix(
        ["a"]) == "a"


def test__() -> None:
    assert Solution().longestCommonPrefix(
        ["", ""]) == ""


def test_a_() -> None:
    assert Solution().longestCommonPrefix(
        ["a", ""]) == ""


def test__a() -> None:
    assert Solution().longestCommonPrefix(
        ["", "a"]) == ""


def test_a_b() -> None:
    assert Solution().longestCommonPrefix(
        ["a", "b"]) == ""


def test_a_a() -> None:
    assert Solution().longestCommonPrefix(
        ["a", "a"]) == "a"


def test_a_ab() -> None:
    assert Solution().longestCommonPrefix(
        ["a", "ab"]) == "a"


def test_ab_a() -> None:
    assert Solution().longestCommonPrefix(
        ["ab", "a"]) == "a"


def test_ab_ac() -> None:
    assert Solution().longestCommonPrefix(
        ["ab", "ac"]) == "a"


def test_a_aa() -> None:
    assert Solution().longestCommonPrefix(
        ["a", "aa"]) == "a"


def test_aa_a() -> None:
    assert Solution().longestCommonPrefix(
        ["aa", "a"]) == "a"


def test_aa_aa() -> None:
    assert Solution().longestCommonPrefix(
        ["aa", "aa"]) == "aa"


def test_a_a_b() -> None:
    assert Solution().longestCommonPrefix(
        ["a", "a", "b"]) == ""


def test_aa_ab_ac() -> None:
    assert Solution().longestCommonPrefix(
        ["aa", "ab", "ac"]) == "a"

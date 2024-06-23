#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4Sum II.

https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1134/
Created on Thu Jun  6 08:35:55 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from timer import timer


class Solution:
    """Leetcode class for answers."""

    @timer
    def decodeString(self,  # pylint: disable=invalid-name
                     s: str) -> str:
        """Leetcode function as answer."""
        stack: deque[tuple[str, str]] = deque()
        lavel = word = number = ""

        def new_lavel() -> None:
            nonlocal lavel, word, number
            stack.append((number, lavel + word))
            lavel = word = number = ""

        def end_lavel() -> None:
            nonlocal lavel, word, number
            word = lavel + word
            number, lavel = stack.pop()
            lavel = int(number) * (lavel + word)
            number = word = ""

        def upd_lavel() -> None:
            nonlocal lavel, word, number
            word = lavel + word
            number, lavel = "1", ""
            if stack:
                number, lavel = stack.pop()
            new_lavel()

        for char in s:

            if char.isdigit():
                if word or lavel:
                    upd_lavel()
                number += char

            elif char == "[":
                new_lavel()

            elif char.isalpha():
                word += char

            elif char == "]":
                end_lavel()

        lavel += word
        while stack:
            _, word = stack.pop()
            lavel = word + lavel

        return lavel


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().decodeString)
    print("result:", func_timed("2[abc]3[cd]ef"))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().decodeString(
        "3[a]2[bc]") == "aaabcbc"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().decodeString(
        "3[a2[c]]") == "accaccacc"


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().decodeString(
        "2[abc]3[cd]ef") == "abcabccdcdcdef"


def test_common() -> None:
    func = Solution().decodeString

    assert func("a") == "a"
    assert func("ab") == "ab"
    assert func("1[a]") == "a"
    assert func("2[a]") == "aa"
    assert func("a2[b]") == "abb"
    assert func("2[a]b") == "aab"
    assert func("a2[b]c") == "abbc"
    assert func("2[a]b2[c]") == "aabcc"
    assert func("2[a]bc2[d]e") == "aabcdde"
    assert func("2[a]2[b]cd3[e]") == "aabbcdeee"
    assert func("1[a2[b]]") == "abb"
    assert func("3[a2[b]]") == "abbabbabb"
    assert func("1[a1[b1[c]]]") == "abc"
    assert func("1[ab1[c1[d]2[f]]]") == "abcdff"

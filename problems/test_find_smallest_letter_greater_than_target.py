#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find Smallest Letter Greater Than Target.

https://leetcode.com/explore/learn/card/binary-search/137/conclusion/977/
Created on Thu Jun  6 08:35:55 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from bisect import bisect_right
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def nextGreatestLetter(self,  # pylint: disable=invalid-name
                           letters: list[str], target: str) -> str:
        """Leetcode function as answer."""
        point = bisect_right(letters, target)
        if point == len(letters):
            return letters[0]
        return letters[point]


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().nextGreatestLetter)
    print("result:", func_timed(["c", "f", "j"], target="a"))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().nextGreatestLetter(
        ["c", "f", "j"], target="a") == "c"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().nextGreatestLetter(
        ["c", "f", "j"], target="c") == "f"


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().nextGreatestLetter(
        ["x", "x", "y", "y"], target="z") == "x"


def test_common() -> None:
    """The third example in the task."""
    func = Solution().nextGreatestLetter

    assert func(["b", "c"], "a") == "b"
    assert func(["b", "c"], "b") == "c"
    assert func(["b", "c"], "c") == "b"
    assert func(["b", "c"], "d") == "b"

    assert func(["b", "b", "c"], "a") == "b"
    assert func(["b", "b", "c"], "b") == "c"
    assert func(["b", "b", "c"], "c") == "b"
    assert func(["b", "b", "c"], "d") == "b"

    assert func(["b", "c", "c"], "a") == "b"
    assert func(["b", "c", "c"], "b") == "c"
    assert func(["b", "c", "c"], "c") == "b"
    assert func(["b", "c", "c"], "d") == "b"

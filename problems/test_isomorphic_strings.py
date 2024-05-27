#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Isomorphic Strings.

https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1117/
Created on Sun May 26 16:55:03 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def isIsomorphic(self,  # pylint: disable=invalid-name
                     s: str, t: str) -> bool:
        """Leetcode function as answer."""
        history: dict[str, str] = {}
        for i, char in enumerate(s):
            if char in history:
                if history[char] != t[i]:
                    return False
            elif t[i] in history.values():
                return False
            else:
                history[char] = t[i]
        return True


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().isIsomorphic)
    print("result:", func_timed(["a"]*10000, ["a"]*10000))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().isIsomorphic("egg", "add") is True


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().isIsomorphic("foo", "bar") is False


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().isIsomorphic("paper", "title") is True


def test_1() -> None:
    assert Solution().isIsomorphic("abc", "dee") is False


def test_2() -> None:
    assert Solution().isIsomorphic("dee", "abc") is False

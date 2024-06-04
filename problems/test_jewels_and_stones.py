#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find Duplicate Subtrees.

https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1127/
Created on Mon Jun  3 08:51:43 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer
from string import ascii_letters


class Solution:
    """Leetcode class for answers."""

    def numJewelsInStones(self,  # pylint: disable=invalid-name
                          jewels: str, stones: str) -> int:
        """Leetcode function as answer."""
        return sum(1 for char in stones if char in jewels)


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().numJewelsInStones)
    print("result:", func_timed(ascii_letters, ["a"]*50))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().numJewelsInStones(
        "aA", "aAAbbbb") == 3


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().numJewelsInStones(
        "z", "ZZ") == 0

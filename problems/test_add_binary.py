#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add Binary.

https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/
Created on Wed Apr 10 08:54:05 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def addBinary(self,  # pylint: disable=invalid-name
                  a: str, b: str) -> str:
        """Leetcode function as answer."""
        result = int(a, base=2) + int(b, base=2)
        return f"{result:b}"


if __name__ == "__main__":
    func_timed = timer(Solution().addBinary)
    a, b = "11", "1"
    print("result:", func_timed(a, b))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().addBinary(
        "11", "1") == "100"


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().addBinary(
        "1010", "1011") == "10101"


def test_0_0() -> None:
    assert Solution().addBinary(
        "0", "0") == "0"


def test_0_1() -> None:
    assert Solution().addBinary(
        "0", "1") == "1"


def test_1_1() -> None:
    assert Solution().addBinary(
        "1", "1") == "10"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guess Number Higher or Lower.

https://leetcode.com/explore/learn/card/binary-search/125/template-i/951/
Created on Sun Jun 30 08:50:17 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


def guess(num: int) -> int:
    """Leetcode API."""
    return 0


class Solution:
    """Leetcode class for answers."""

    pick: int

    def __init__(self, pick: int) -> None:
        global guess
        self.pick = pick
        guess = self._guess

    def _guess(self, num: int) -> int:
        """Compare num with pick."""
        if num > self.pick:
            return -1
        if num < self.pick:
            return 1
        return 0

    def guessNumber(self,  # pylint: disable=invalid-name
                    n: int) -> int:
        """Leetcode function as answer."""
        left, right = 1, n
        while True:
            cur = left + (right-left)//2
            check = guess(cur)
            # print("cur:", cur, "check:", check)
            if check == 0:
                return cur

            if check == 1:
                left = cur + 1
            elif check == -1:
                right = cur - 1


if __name__ == "__main__":
    func_timed = timer(Solution(1).guessNumber)
    print("result:", func_timed(2**31))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution(6).guessNumber(
        10) == 6


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution(1).guessNumber(
        1) == 1


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution(1).guessNumber(
        2) == 1

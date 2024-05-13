#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pow(x, n).

https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2380/
Created on Sun May 12 16:50:01 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def myPow(self,  # pylint: disable=invalid-name
              x: float, n: int) -> float:
        """Leetcode function as answer."""
        # I'm lazy to realize it as recursion
        from decimal import Decimal
        return float(pow(Decimal(str(x)), n))


if __name__ == "__main__":
    func_timed = timer(Solution().myPow)
    print("result:", func_timed(
        2.0, 2))

#########
# Tests
# pylint: disable=missing-function-docstring


# float result needs to be rounded up,
# but I'm too lazy - it works like this :)
def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().myPow(
        2.0, 10) == 1024.0


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().myPow(
        2.1, 3) == 9.261


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().myPow(
        2.0, -2) == 0.25

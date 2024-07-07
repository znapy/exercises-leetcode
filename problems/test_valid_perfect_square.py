#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Valid Perfect Square.

https://leetcode.com/explore/learn/card/binary-search/137/conclusion/978/
Created on Sat Jul  6 20:49:09 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def isPerfectSquare(self,  # pylint: disable=invalid-name
                        num: int) -> bool:
        """Leetcode function as answer."""
        if num == 1:
            return True
        low, high = 2, num
        while low < high:
            mid = low + (high-low)//2
            square = mid*mid
            if square > num:
                high = mid
            elif square == num:
                return True
            else:
                low = mid+1
        return False


if __name__ == "__main__":
    func_timed = timer(Solution().isPerfectSquare)
    print("result:", func_timed(2_147_395_600))
    print("built-in:", timer(pow)(2_147_395_600, 0.5))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().isPerfectSquare(16) is True


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().isPerfectSquare(14) is False


def test_common() -> None:
    f = Solution().isPerfectSquare
    # my
    assert f(1) is True
    assert f(2) is False
    assert f(3) is False
    assert f(4) is True
    assert f(5) is False
    assert f(6) is False
    assert f(7) is False
    assert f(8) is False
    assert f(9) is True
    assert f(2_147_395_600) is True
    assert f(2_147_395_601) is False

    # Leetcode unittest 1
    # assert f([1, 6, 5, 4, 3, 2, 1]) == 1

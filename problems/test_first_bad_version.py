#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
First Bad Version.

https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/
Created on Sun Jun 30 10:23:05 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


def isBadVersion(  # pylint: disable=invalid-name
                 version: int) -> bool:
    """Leetcode API."""
    return True


class Solution:
    """Leetcode class for answers."""

    first_bad: int

    def __init__(self, first_bad: int) -> None:
        global isBadVersion
        self.first_bad = first_bad
        isBadVersion = self._is_bad_version

    def _is_bad_version(self, version: int) -> bool:
        """Compare version with pick."""
        if version >= self.first_bad:
            return True
        return False

    def firstBadVersion(self,  # pylint: disable=invalid-name
                        n: int) -> int:
        """Leetcode function as answer."""
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
            # print("mid", mid, "check", check)

        return right  # There is at list one bad version


if __name__ == "__main__":
    func_timed = timer(Solution(1).firstBadVersion)
    print("result:", func_timed(2**31))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution(4).firstBadVersion(
        5) == 4


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution(1).firstBadVersion(
        1) == 1

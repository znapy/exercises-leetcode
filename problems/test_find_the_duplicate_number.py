#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find the Duplicate Number.

https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1039/
Created on Tue Jul  9 08:58:55 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import Counter
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def findDuplicate(self,  # pylint: disable=invalid-name
                      nums: list[int]) -> int:
        """Leetcode function as answer."""
        return Counter(nums).most_common(1)[0][0]


if __name__ == "__main__":
    func_timed = timer(Solution().findDuplicate)
    print("result:", func_timed([1, 3, 4, 2, 2]))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().findDuplicate(
        [1, 3, 4, 2, 2]) == 2


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().findDuplicate(
        [3, 1, 3, 4, 2]) == 3


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().findDuplicate(
        [3, 3, 3, 3, 3]) == 3

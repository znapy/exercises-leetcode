#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Single Number.

https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/
Created on Wed May 22 08:04:34 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def singleNumber(self,  # pylint: disable=invalid-name
                     nums: list[int]) -> int:
        """Leetcode function as answer."""
        history: set[int] = set()
        for val in nums:
            if val in history:
                history.remove(val)
                continue
            history.add(val)
        return history.pop()


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().singleNumber)
    nums = list(range(15000)) + list(range(14999))
    print("result:", func_timed(nums))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().singleNumber([2, 2, 1]) == 1


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().singleNumber([1]) == 1

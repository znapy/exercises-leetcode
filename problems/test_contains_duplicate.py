#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains Duplicate.

https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/
Created on Mon May 20 08:50:29 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def containsDuplicate(self,  # pylint: disable=invalid-name
                          nums: list[int]) -> bool:
        """Leetcode function as answer."""
        history = set()
        for val in nums:
            if val in history:
                return True
            history.add(val)
        return False


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().containsDuplicate)
    print("result:", func_timed(val for val in range(99999)))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().containsDuplicate([1, 2, 3, 1]) is True


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().containsDuplicate([1, 2, 3, 4]) is False


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
                                        ) is True

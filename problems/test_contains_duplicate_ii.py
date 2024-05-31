#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains Duplicate II.

https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1121/
Created on Wed May 29 09:14:48 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def containsNearbyDuplicate(self,  # pylint: disable=invalid-name
                                nums: list[int], k: int) -> bool:
        """Leetcode function as answer."""
        duplicates: dict[int, int] = dict()
        for i, val in enumerate(nums):
            prev = duplicates.get(val, None)
            if prev is not None and i - prev <= k:
                return True
            duplicates[val] = i

        return False


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().containsNearbyDuplicate)
    print("result:", func_timed(range(100000), 100000))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().containsNearbyDuplicate(
        [1, 2, 3, 1], 3) is True


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().containsNearbyDuplicate(
        [1, 0, 1, 1], 1) is True


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().containsNearbyDuplicate(
        [1, 2, 3, 1, 2, 3], 2) is False

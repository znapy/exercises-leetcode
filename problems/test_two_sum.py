#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Two Sum.

https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1115/
Created on Fri May 24 14:40:54 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import defaultdict
from typing import DefaultDict
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def twoSum(self,  # pylint: disable=invalid-name
               nums: list[int], target: int) -> list[int]:
        """Leetcode function as answer."""
        hashmap: DefaultDict[int, list[int]] = defaultdict(list)

        def get_another_index(n: int, index: int) -> int:
            for result in hashmap[n]:
                if result != index:
                    return result
            return -1

        for i, num in enumerate(nums):
            hashmap[num].append(i)
        for i, num in enumerate(nums):
            augend = get_another_index(target - num, i)
            if augend != -1:
                return [i, augend]
        return []


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().twoSum)
    nums = list(range(9998)) + [9997]
    print("result:", func_timed(nums, 10000))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().twoSum([3, 3], 6) == [0, 1]

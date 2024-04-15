#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Array Partition I.

https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/
Created on Mon Apr 15 10:18:20 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from itertools import permutations
from typing import Iterable, cast
from timer import timer


class Solution:
    """Leetcode class for answers."""

    @staticmethod
    def batched(iterable: Iterable[int],
                n: int  # for our task n is always 2
                ) -> Iterable[tuple[int, int]]:
        """Batch data from the iterable into tuples of length n."""
        # The "batched" function is implemented in python 3.12
        #   but leetcode use version 3.11.
        # For our task the iterable is nonempty and always even
        prev: int | None = None
        for cur in iterable:
            if prev is None:
                prev = cur
                continue
            yield (prev, cur)
            prev = None

    @staticmethod
    def sum_of_mins(pairs: Iterable[int]) -> int:
        """Calculate sum of the minimum value from the pairs."""
        result = 0
        for batch in Solution.batched(pairs, 2):
            result += min(batch)
        return result

    @timer
    def brute(self, nums: list[int]) -> int:
        """Bruteforce solution."""
        result: int | None = None
        for deck in permutations(nums, len(nums)):
            if result is None:
                result = self.sum_of_mins(deck)
            else:
                result = max(result,
                             self.sum_of_mins(deck))
        return cast(int, result)

    def arrayPairSum(self,  # pylint: disable=invalid-name
                     nums: list[int]) -> int:
        """Leetcode function as answer."""
        return Solution.sum_of_mins(sorted(nums))
        # In ordered pairs first element is always minimal
        #   so we can take sum(sorted(nums)[::2]).
        # Why this task is in two-pointer unit?


if __name__ == "__main__":
    func_timed = timer(Solution().arrayPairSum)
    nums = [1, 4, 3, 2]
    print("result:", result := func_timed(nums),
          "brute:", result2 := Solution().brute(nums))
    assert result == result2

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().arrayPairSum(
        [1, 4, 3, 2]) == 4


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().arrayPairSum(
        [6, 2, 6, 5, 1, 2]) == 9


def test_0_0() -> None:
    assert Solution().arrayPairSum(
        [0, 0]) == 0


def test_0_minus_1() -> None:
    assert Solution().arrayPairSum(
        [0, -1]) == -1


def test_1_minus_1_twice() -> None:
    assert Solution().arrayPairSum(
        [1, -1, 1, -1]) == 0

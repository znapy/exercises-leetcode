#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Squares of a Sorted Array.

https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
Created on Wed Mar 22 11:27:02 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    @timer
    def sorted_squares_brute(self, nums: list[int]) -> list[int]:
        """Squares of a Sorted Array - simpliest."""
        return sorted(num*num for num in nums)

    def sortedSquares(self,  # pylint: disable=invalid-name
                      nums: list[int]) -> list[int]:
        """Leetcode function as answer."""
        res: list[int] = []
        cur = 0
        for num in nums:
            element = num*num

            len_res = len(res)
            while cur < len_res:
                if element > res[cur]:
                    cur += 1
                else:
                    break
            res.insert(cur, element)

        return res


if __name__ == "__main__":
    func_timed = timer(Solution().sortedSquares)
    nums = [-4, -4, -3]  # [-4, -1, 0, 3, 10]  # [-2, -1, 0, 3, 4]
    print("sortedSquares:", func_timed(nums))
    print("sorted_squares_brute:", Solution().sorted_squares_brute(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().sortedSquares(
        [-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().sortedSquares(
        [-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

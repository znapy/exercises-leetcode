#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Squares of a Sorted Array.

https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
Created on Wed Mar 22 11:27:02 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""


class Solution:
    """Leetcode class for answers."""

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

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """Fhe first example in the task."""
    assert Solution().sortedSquares(
        [-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


def test_leetcode_example_2() -> None:
    """Fhe second example in the task."""
    assert Solution().sortedSquares(
        [-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

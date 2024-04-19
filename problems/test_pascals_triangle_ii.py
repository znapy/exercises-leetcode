#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add Binary.

https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/
Created on Wed Apr 10 08:54:05 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer
from math import factorial


class Solution:
    """Leetcode class for answers."""

    def getRow(self,  # pylint: disable=invalid-name
               rowIndex: int) -> list[int]:
        """Leetcode function as answer."""
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        result: list[int] = [1, 1]
        n = rowIndex
        fact_n = factorial(n)
        center = (n+1) // 2
        center_plus = (n+1) % 2
        for m in range(1, center + center_plus):

            if m == 1:
                val = n
            else:
                denominator = factorial(m) * factorial(n-m)
                val = int(fact_n / denominator)

            result.insert(m, val)
            print(m, val)

            if m < center:
                result.insert(len(result)-m, val)

        return result
        # Leetcode solution:
        # res = [1]*(rowIndex+1)
        # for i in range(2, rowIndex+1):
        #     prev = res[0]
        #     for j in range(1,i):
        #         tmp = res[j]
        #         res[j] = prev+res[j]
        #         prev = tmp
        # return res


if __name__ == "__main__":
    func_timed = timer(Solution().getRow)
    rowIndex = 3
    print("result:", func_timed(rowIndex))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().getRow(
        3) == [1, 3, 3, 1]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().getRow(
        0) == [1]


def test_leetcode_example_3() -> None:
    """The second example in the task."""
    assert Solution().getRow(
        1) == [1, 1]


def test_2() -> None:
    assert Solution().getRow(
        2) == [1, 2, 1]


def test_4() -> None:
    assert Solution().getRow(
        4) == [1, 4, 6, 4, 1]

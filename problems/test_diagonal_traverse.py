#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Diagonal Traverse.

https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
Created on Mon Apr  8 08:40:47 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from typing import Iterator
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def findDiagonalOrder(self,  # pylint: disable=invalid-name
                          mat: list[list[int]]) -> list[int]:
        """Leetcode function as answer."""
        def idx(m: int, n: int) -> Iterator[tuple[int, int]]:
            """Generate iterator throw indexes."""
            i, j, step = 0, 0, -1

            while True:
                yield (i, j)
                if i + 1 == m and j + 1 == n:
                    break
                i += step
                j -= step
                kick = False
                if i < 0:
                    i = 0
                    kick = True
                if j < 0:
                    j = 0
                    kick = True
                if i == m:
                    i -= 1
                    j += 1 if kick else 2
                    kick = True
                if j == n:
                    j -= 1
                    i += 1 if kick else 2
                    kick = True
                if kick:
                    step = -step

        result: list[int] = []
        for i, j in idx(len(mat), len(mat[0])):
            result.append(mat[i][j])
        return result
        # We can also use fact: i+j in each diagonale is the same.
        # So use collections.defaultdict(list) to store each diagonale values
        # and reverse odd diagonals


if __name__ == "__main__":
    func_timed = timer(Solution().findDiagonalOrder)
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("result:", func_timed(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().findDiagonalOrder(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 4, 7, 5, 3, 6, 8, 9]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().findDiagonalOrder(
        [[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_1_() -> None:
    assert Solution().findDiagonalOrder(
        [[1]]) == [1]


def test_1_2_() -> None:
    assert Solution().findDiagonalOrder(
        [[1], [2]]) == [1, 2]


def test_12_() -> None:
    assert Solution().findDiagonalOrder(
        [[1, 2]]) == [1, 2]


def test_1_2_3_() -> None:
    assert Solution().findDiagonalOrder(
        [[1], [2], [3]]) == [1, 2, 3]


def test_12_34_56_() -> None:
    assert Solution().findDiagonalOrder(
        [[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 5, 4, 6]


def test_123_456_() -> None:
    assert Solution().findDiagonalOrder(
        [[1, 2, 3], [4, 5, 6]]) == [1, 2, 4, 5, 3, 6]

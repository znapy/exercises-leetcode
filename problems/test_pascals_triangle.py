#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pascal's Triangle.

https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/
Created on Tue Apr  9 10:26:44 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def generate(self,  # pylint: disable=invalid-name
                 numRows: int) -> list[list[int]]:
        """Leetcode function as answer."""
        result = [[1]]
        if numRows == 1:
            return result

        result.append([1, 1])
        if numRows == 2:
            return result

        for i in range(1, numRows-1):
            prev: int | None = None
            row = [1]
            for val in result[i]:
                if prev is not None:
                    row.append(prev + val)
                prev = val
            row.append(1)
            result.append(row)
        return result


if __name__ == "__main__":
    func_timed = timer(Solution().generate)
    print("result:", func_timed(3))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().generate(
        5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().generate(
        1) == [[1]]


def test_2() -> None:
    assert Solution().generate(
        2) == [[1], [1, 1]]


def test_3() -> None:
    assert Solution().generate(
        3) == [[1], [1, 1], [1, 2, 1]]


def test_4() -> None:
    assert Solution().generate(
        4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

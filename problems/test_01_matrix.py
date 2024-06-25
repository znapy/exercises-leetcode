#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01 Matrix.

https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1388/
Created on Mon Jun 24 08:09:44 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def updateMatrix(self,  # pylint: disable=invalid-name
                     mat: list[list[int]]) -> list[list[int]]:
        """Leetcode function as answer."""
        result: dict[tuple[int, int], int] = {}
        candidates: set[tuple[int, int]] = set()
        rest: set[tuple[int, int]] = set()
        m, n = len(mat), len(mat[0])

        def neightbors(i: int, j: int) -> list[tuple[int, int]]:
            result: list[tuple[int, int]] = []
            if i > 0:
                result.append((i-1, j))
            if j > 0:
                result.append((i, j-1))
            if i+1 < m:
                result.append((i+1, j))
            if j+1 < n:
                result.append((i, j+1))
            return result

        for i, row in enumerate(mat):
            for j, val in enumerate(row):

                if val == 0:
                    result[(i, j)] = 0
                    for neightbor in neightbors(i, j):
                        if neightbor not in result:
                            candidates.add(neightbor)

                elif val == 1:
                    rest.add((i, j))

        step = 1
        while rest:
            candidates_prev, candidates = candidates, set()
            for i, j in candidates_prev:
                if (i, j) in result:
                    continue
                result[i, j] = step
                rest.remove((i, j))
                for neightbor in neightbors(i, j):
                    if neightbor not in result:
                        candidates.add(neightbor)
            step += 1

        return [[result[i, j] for j in range(n)] for i in range(m)]


if __name__ == "__main__":
    func_timed = timer(Solution().updateMatrix)
    a, b = "11", "1"
    print("result:", func_timed([[0, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 0]]))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().updateMatrix(
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == \
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().updateMatrix(
        [[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == \
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]]


def test_0() -> None:
    assert Solution().updateMatrix(
        [[0]]) == [[0]]


def test_0_0() -> None:
    assert Solution().updateMatrix(
        [[0, 0]]) == [[0, 0]]


def test_common() -> None:
    func = Solution().updateMatrix
    assert func([[0], [0]]) == [[0], [0]]
    assert func([[0, 1]]) == [[0, 1]]
    assert func([[1, 0]]) == [[1, 0]]
    assert func([[0], [1]]) == [[0], [1]]
    assert func([[1], [0]]) == [[1], [0]]

    assert func([[0, 0], [0, 0]]) == [[0, 0], [0, 0]]
    assert func([[0, 1], [0, 0]]) == [[0, 1], [0, 0]]
    assert func([[0, 0], [1, 0]]) == [[0, 0], [1, 0]]
    assert func([[0, 0], [0, 1]]) == [[0, 0], [0, 1]]
    assert func([[1, 0], [0, 0]]) == [[1, 0], [0, 0]]
    assert func([[0, 1], [1, 0]]) == [[0, 1], [1, 0]]
    assert func([[0, 1], [0, 1]]) == [[0, 1], [0, 1]]
    assert func([[0, 0], [1, 1]]) == [[0, 0], [1, 1]]
    assert func([[1, 1], [0, 0]]) == [[1, 1], [0, 0]]
    assert func([[1, 0], [1, 0]]) == [[1, 0], [1, 0]]
    assert func([[1, 0], [0, 1]]) == [[1, 0], [0, 1]]
    assert func([[1, 1], [1, 0]]) == [[2, 1], [1, 0]]
    assert func([[1, 1], [0, 1]]) == [[1, 2], [0, 1]]
    assert func([[1, 0], [1, 1]]) == [[1, 0], [2, 1]]

    assert func([[0, 0], [0, 0], [0, 0]]) == [[0, 0], [0, 0], [0, 0]]
    assert func([[1, 0], [0, 0], [0, 0]]) == [[1, 0], [0, 0], [0, 0]]
    assert func([[0, 0], [0, 0], [0, 1]]) == [[0, 0], [0, 0], [0, 1]]
    assert func([[1, 1], [1, 1], [0, 0]]) == [[2, 2], [1, 1], [0, 0]]
    assert func([[1, 1], [1, 0], [1, 0]]) == [[2, 1], [1, 0], [1, 0]]
    assert func([[1, 1], [1, 0], [0, 1]]) == [[2, 1], [1, 0], [0, 1]]
    assert func([[1, 1], [1, 1], [0, 1]]) == [[2, 3], [1, 2], [0, 1]]
    assert func([[1, 1], [1, 1], [1, 0]]) == [[3, 2], [2, 1], [1, 0]]

    assert func([[0, 0, 0], [0, 0, 0]]) == [[0, 0, 0], [0, 0, 0]]
    assert func([[0, 1, 0], [0, 0, 0]]) == [[0, 1, 0], [0, 0, 0]]
    assert func([[0, 1, 0], [0, 1, 0]]) == [[0, 1, 0], [0, 1, 0]]
    assert func([[0, 1, 1], [0, 1, 1]]) == [[0, 1, 2], [0, 1, 2]]
    assert func([[1, 1, 1], [0, 1, 1]]) == [[1, 2, 3], [0, 1, 2]]

    assert func(
        [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 0]]) == \
        [[5, 4, 3], [4, 3, 2], [3, 2, 1], [2, 1, 0]]

    assert func(
        [[0, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 0]]) == \
        [[0, 1, 2], [1, 2, 2], [2, 2, 1], [2, 1, 0]]

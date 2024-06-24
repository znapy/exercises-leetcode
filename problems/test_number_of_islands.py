#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Number of Islands.

https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/
Created on Mon Jun 10 09:13:37 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def numIslands(self,  # pylint: disable=invalid-name
                   grid: list[list[str]]) -> int:
        """Leetcode function as answer."""
        # Leetcode solution - mark visited cells as "0" in grid:
        # n, m = len(A), len(A[0])

        # def dfs(i, j):
        #     if not (0 <= i < n and 0 <= j < m and A[i][j] == '1'): return 0
        #     A[i][j] = '0'
        #     for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        #         dfs(i + di, j + dj)
        #     return 1

        # return sum(dfs(i, j) for i in range(n) \
        #            for j in range(m) if A[i][j] == "1")
        size = (len(grid), len(grid[0]))
        Point = tuple[int, int]
        unstepped: set[Point] = set()
        unstepped_size = size[0] * size[1]
        for i in range(size[0]):
            for j in range(size[1]):
                unstepped.add((i, j))

        result = 0

        def neighbors(point_i: int, point_j: int) -> list[Point]:
            neighbors: list[Point] = []

            i, j = point_i - 1, point_j
            if i >= 0 and (i, j) in unstepped:
                neighbors.append((i, j))

            i, j = point_i + 1, point_j
            if i < size[0] and (i, j) in unstepped:
                neighbors.append((i, j))

            i, j = point_i, point_j - 1
            if j >= 0 and (i, j) in unstepped:
                neighbors.append((i, j))

            i, j = point_i, point_j + 1
            if j < size[1] and (i, j) in unstepped:
                neighbors.append((i, j))

            return neighbors

        def step(unstepped_size: int,
                 queue: deque[Point], point_i: int, point_j: int) -> int:
            unstepped_size -= 1

            if grid[point_i][point_j] == "0":
                return unstepped_size

            for neighbor in neighbors(point_i, point_j):
                if neighbor not in queue:
                    queue.append(neighbor)

            return unstepped_size

        queue: deque[Point] = deque()
        while unstepped_size:
            i, j = unstepped.pop()
            if grid[i][j] == "1":
                result += 1

            unstepped_size = step(unstepped_size, queue, i, j)
            while len(queue):
                i, j = queue.pop()
                unstepped.remove((i, j))
                unstepped_size = step(unstepped_size, queue, i, j)

        return result


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().numIslands)
    grid = [
      ["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]
    ]

    print("result:", func_timed(grid))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().numIslands(
        [
          ["1", "1", "1", "1", "0"],
          ["1", "1", "0", "1", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "0", "0", "0"]
        ]) == 1


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().numIslands(
        [
          ["1", "1", "0", "0", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "1", "0", "0"],
          ["0", "0", "0", "1", "1"]
        ]) == 3


class TestSolution:
    """Test class."""

    @staticmethod
    def test_numIslands(  # pylint: disable=invalid-name
            ) -> None:
        """Leetcode and my testcases."""
        func = Solution().numIslands

        # My
        assert func([["1"]]) == 1
        assert func([["0"]]) == 0

        assert func([["0"], ["1"]]) == 1
        assert func([["0", "1"]]) == 1

        assert func([["1"], ["0"]]) == 1
        assert func([["1", "0"]]) == 1

        assert func([["1"], ["1"]]) == 1
        assert func([["1", "1"]]) == 1

        assert func([["0"], ["0"]]) == 0
        assert func([["0", "0"]]) == 0

        grid = [["0", "0"],
                ["0", "0"]]
        assert func(grid) == 0

        grid = [["1", "0"],
                ["0", "0"]]
        assert func(grid) == 1

        grid = [["1", "1"],
                ["1", "0"]]
        assert func(grid) == 1

        grid = [["1", "0"],
                ["0", "1"]]
        assert func(grid) == 2

        grid = [["0", "0"],
                ["0", "1"]]
        assert func(grid) == 1

        grid = [["1", "0", "1"],
                ["1", "0", "1"],
                ["1", "1", "1"]]
        assert func(grid) == 1

        grid = [["1", "0", "1"],
                ["1", "1", "1"],
                ["1", "0", "1"]]
        assert func(grid) == 1

        grid = [["1", "0", "1"],
                ["0", "1", "0"],
                ["1", "0", "1"]]
        assert func(grid) == 5

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flood Fill.

https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1393/
Created on Sun Jun 23 16:45:05 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from timer import timer


class Solution:
    """Leetcode class for answers."""

    @timer
    def floodFill(self,  # pylint: disable=invalid-name
                  image: list[list[int]], sr: int, sc: int, color: int
                  ) -> list[list[int]]:
        """Leetcode function as answer."""
        result = image.copy()
        size = (len(image), len(image[0]))
        Point = tuple[int, int]
        processed: set[Point] = set()

        def neighbors(point_i: int, point_j: int) -> list[Point]:
            neighbors: list[Point] = []

            i, j = point = point_i - 1, point_j
            if i >= 0 and point not in processed:
                neighbors.append(point)
                processed.add(point)

            i, j = point = point_i + 1, point_j
            if i < size[0] and point not in processed:
                neighbors.append(point)
                processed.add(point)

            i, j = point = point_i, point_j - 1
            if j >= 0 and point not in processed:
                neighbors.append(point)
                processed.add(point)

            i, j = point = point_i, point_j + 1
            if j < size[1] and point not in processed:
                neighbors.append(point)
                processed.add(point)

            return neighbors

        original = image[sr][sc]
        queue: deque[Point] = deque([(sr, sc)])
        while len(queue):
            i, j = queue.pop()
            if image[i][j] == original:
                result[i][j] = color
                queue.extend(neighbors(i, j))

        return result


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().floodFill)
    print("result:", func_timed(
        image=[[1]*50]*50, sr=0, sc=0, color=2))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().floodFill(
        image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]],
        sr=1, sc=1, color=2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().floodFill(
        image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0) == \
        [[0, 0, 0], [0, 0, 0]]


def test_common() -> None:
    func = Solution().floodFill

    assert func(image=[[1]*50]*50, sr=0, sc=0, color=2) == [[2]*50]*50

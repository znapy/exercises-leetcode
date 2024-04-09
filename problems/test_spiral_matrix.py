#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spiral Matrix.

https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/
Created on Mon Apr  8 09:00:53 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from typing import Iterator, cast
from timer import timer


class Solution:
    """Leetcode class for answers."""

    Offset = tuple[int, int]

    offset_clockwise = {(0, 1): (1, 0),
                        (1, 0): (0, -1),
                        (0, -1): (-1, 0),
                        (-1, 0): (0, 1)}
    offset_counterclockwise = {val: key
                               for key, val in offset_clockwise.items()}
    # Rules for each Offset: offset index, corner
    rule = {(0, 1): (1, "corner_right"),
            (1, 0): (0, "corner_bottom"),
            (0, -1): (1, "corner_left"),
            (-1, 0): (0, "corner_top")}

    def cell(self) -> Offset:
        """Current cell for iterator."""
        return cast(Solution.Offset, self.cursor["cell"])

    def step(self) -> Offset:
        """Current direction for iterator."""
        return cast(Solution.Offset, self.cursor["step"])

    def next_cell(self) -> Offset:
        """Next point from cursors cell and step."""
        row, column = self.cell()
        right, down = self.step()
        return (row + right, column + down)

    def rotate(self, clockwise: bool = True) -> Offset:
        """Next offset after rotation."""
        step = self.step()
        if clockwise:
            return Solution.offset_clockwise[step]
        return Solution.offset_counterclockwise[step]

    def in_direction(self) -> bool:
        """Check next cell in the current direction."""
        cell = self.next_cell()
        index, corner = self.rule[self.step()]

        if cell[index] == self.cursor[corner]:
            return False

        self.cursor["cell"] = cell
        return True

    def in_rotation(self) -> bool:
        """Check next cell after rotation."""
        # Update corner
        previous_offset = self.rotate(clockwise=False)
        previous_rule = self.rule[previous_offset]
        self.cursor[previous_rule[1]] = self.cell()[previous_rule[0]]

        self.cursor["step"] = self.rotate()

        return self.in_direction()

    def idx(self, m: int, n: int) -> Iterator[Offset]:
        """Generate iterator throw indexes."""

        self.cursor = {
            "corner_left": -1,
            "corner_top": -1,
            "corner_right": n,
            "corner_bottom": m,
            "cell": (0, -1),  # current row and column
            "step": (0, 1)  # next offset of row and column
            }

        while True:

            if self.in_direction() or self.in_rotation():
                yield self.cell()
            else:
                break

    def spiralOrder(self,  # pylint: disable=invalid-name
                    matrix: list[list[int]]) -> list[int]:
        """Leetcode function as answer."""
        result: list[int] = []
        for i, j in self.idx(len(matrix), len(matrix[0])):
            result.append(matrix[i][j])
        return result
        # We can also use everything in one loop with corners
        # and 4 directions in each pass


if __name__ == "__main__":
    func_timed = timer(Solution().spiralOrder)
    nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print("result:", func_timed(nums))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().spiralOrder(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().spiralOrder(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == \
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def test_1() -> None:
    assert Solution().spiralOrder(
        [[1]]) == [1]


def test_12() -> None:
    assert Solution().spiralOrder(
        [[1, 2]]) == [1, 2]


def test_1_2() -> None:
    assert Solution().spiralOrder(
        [[1], [2]]) == [1, 2]


def test_12_34() -> None:
    assert Solution().spiralOrder(
        [[1, 2], [3, 4]]) == [1, 2, 4, 3]


def test_123_456() -> None:
    assert Solution().spiralOrder(
        [[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 6, 5, 4]


def test_12_34_56() -> None:
    assert Solution().spiralOrder(
        [[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]

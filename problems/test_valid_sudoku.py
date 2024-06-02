#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Valid Sudoku.

https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1126/
Created on Sun Jun  2 12:31:56 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def isValidSudoku(self,  # pylint: disable=invalid-name
                      board: list[list[str]]) -> bool:
        """Leetcode function as answer."""
        # Check rows
        for row in board:
            row_clean = [x for x in row if x != "."]
            if len(row_clean) != len(set(row_clean)):
                return False

        # Check columns
        for i in range(len(board)):
            col_clean = [x[i] for x in board if x[i] != '.']
            if len(col_clean) != len(set(col_clean)):
                return False

        # Check sub-boxes (3*3)
        for i_modificator in range(3):
            for j_modificator in range(3):
                box_clean = []
                for i_cur in range(3):
                    for j_cur in range(3):
                        i = i_cur + i_modificator*3
                        j = j_cur + j_modificator*3
                        val = board[i][j]
                        if val != ".":
                            box_clean.append(val)
                if len(box_clean) != len(set(box_clean)):
                    return False

        return True


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().isValidSudoku)
    board = \
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print("result:", func_timed(board))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is True


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().isValidSudoku(
        [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]) is False

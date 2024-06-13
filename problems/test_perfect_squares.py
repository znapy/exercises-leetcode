#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Perfect Squares.

https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/
Created on Wed Jun 12 09:25:57 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from itertools import combinations_with_replacement
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def numSquares(self,  # pylint: disable=invalid-name
                   n: int) -> int:
        """Leetcode function as answer."""
        squares: set[int] = set()
        two = False
        for i in range(1, n):
            square = i**2
            if square == n:
                return 1
            if square > n:
                break
            dif = n - square
            if dif == square or dif in squares:
                two = True
            squares.add(square)

        if two:
            return 2

        for result in range(3, n):
            for vals in combinations_with_replacement(squares, result):
                sum_vals = sum(vals)
                if sum_vals == n:
                    return result

        return n
        # Leetcode solution (throw BFS):
        # queue = collections.deque([(0, 0)])
        # visited = set()
        # while queue:
        #     i, step = queue.popleft()
        #     step += 1
        #     for j in xrange(1, n + 1):
        #         k = i + j * j
        #         if k > n:
        #             break
        #         if k == n:
        #             return step
        #         if k not in visited:
        #             visited.add(k)
        #             queue.append((k, step))


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().numSquares)

    print("result:", func_timed(9999))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().numSquares(12) == 3


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().numSquares(13) == 2


def test_leetcode_unittest_1() -> None:
    assert Solution().numSquares(4) == 1


def test_leetcode_unittest_2() -> None:
    assert Solution().numSquares(25) == 1

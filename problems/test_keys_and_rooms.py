#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keys and Rooms.

https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1391/
Created on Wed Jun 26 12:54:19 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def canVisitAllRooms(self,  # pylint: disable=invalid-name
                         rooms: list[list[int]]) -> bool:
        """Leetcode function as answer."""
        keys: deque[int] = deque(rooms[0])
        visited: set[int] = {0}
        while keys:
            cur = keys.pop()
            if cur in visited:
                continue

            visited.add(cur)
            for key in rooms[cur]:
                if key not in visited:
                    keys.append(key)

        return len(visited) == len(rooms)


if __name__ == "__main__":
    func_timed = timer(Solution().canVisitAllRooms)
    print("result:", func_timed([[1], [2], [3], []]))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().canVisitAllRooms(
        [[1], [2], [3], []]) is True


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().canVisitAllRooms(
        [[1, 3], [3, 0, 1], [2], [0]]) is False


def test_common() -> None:
    func = Solution().canVisitAllRooms
    assert func([[], []]) is False
    assert func([[0], []]) is False
    assert func([[], [0]]) is False
    assert func([[1], []]) is True
    assert func([[], [1]]) is False
    assert func([[1], [0], []]) is False
    assert func([[1], [], []]) is False
    assert func([[2], [], []]) is False
    assert func([[2], [], [0]]) is False
    assert func([[2], [], [0, 2]]) is False
    assert func([[2], [], [0, 2, 1]]) is True
    assert func([[2, 2, 2], [], [0, 2]]) is False
    assert func([[1, 2], [], []]) is True

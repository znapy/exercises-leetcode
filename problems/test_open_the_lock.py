#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open the Lock.

https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1375/
Created on Wed Jun 12 09:10:14 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from typing import cast
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def openLock(self,  # pylint: disable=invalid-name
                 deadends: list[str], target: str) -> int:
        """Leetcode function as answer."""
        State = tuple[int, int, int, int]
        current: State = (0, 0, 0, 0)
        dxs = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
               (-1, 0, 0, 0), (0, -1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1)]
        visited: set[State] = set()
        for s in deadends:
            state: list[int] = []
            for char in s:
                state.append(int(char))
            visited.add(cast(State, tuple(state)))
        target_int: State = cast(State, tuple((int(x) for x in target)))

        def neighbors() -> list[State]:
            neighbors: list[State] = []
            for dx in dxs:
                neighbor: State = tuple(  # type: ignore[assignment]
                    x % 10                # type: ignore[operator]
                    for x in map(sum,     # type: ignore[arg-type]
                                 zip(current, dx)))
                if neighbor not in visited:
                    visited.add(neighbor)
                    neighbors.append(neighbor)

            return neighbors

        queue: deque[tuple[State, int]] = deque([(current, 0)])
        while len(queue):
            current, steps = queue.popleft()
            if current == target_int:
                return steps
            for neighbor in neighbors():
                queue.append((neighbor, steps+1))

        return -1


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().openLock)
    deadends = ["0201", "0101", "0102", "1212", "2002"]

    print("result:", func_timed(deadends, "0202"))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    assert Solution().openLock(
        deadends, "0202") == 6


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    assert Solution().openLock(
        deadends, "0202") == 6


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    assert Solution().openLock(
        deadends, "8888") == -1

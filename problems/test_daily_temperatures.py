#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily Temperatures.

https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/
Created on Sat Jun 15 08:32:48 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def dailyTemperatures(self,  # pylint: disable=invalid-name
                          temperatures: list[int]) -> list[int]:
        """Leetcode function as answer."""
        maximals: list[tuple[int, int]] = []  # max and removes before it
        result: list[int] = []
        for val in reversed(temperatures):
            steps, found = 0, False
            for cur_max, removes in reversed(maximals):

                steps += 1

                if cur_max <= val:
                    steps += removes
                    maximals.pop()

                if cur_max > val:
                    found = True
                    break

            maximals.append((val, 0 if steps == 0 else steps - 1))

            result.insert(0, steps if found else 0)

        return result
        # Leetcode solution - remember index of stacked value:
        # res, stack = [0]*len(temperatures), []

        # for i in range(len(temperatures)):
        #     while stack and temperatures[stack[-1]] < temperatures[i]:
        #         prev_day = stack.pop()
        #         res[prev_day] = i - prev_day

        #     stack.append(i)

        # return res


if __name__ == "__main__":
    func_timed = timer(Solution().dailyTemperatures)
    print("result:", func_timed([73, 74, 75, 71, 69, 72, 76, 73]))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().dailyTemperatures(
        [73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().dailyTemperatures(
        [30, 40, 50, 60]) == [1, 1, 1, 0]


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().dailyTemperatures(
        [30, 60, 90]) == [1, 1, 0]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluate Reverse Polish Notation.

https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1394/
Created on Sun Jun 16 07:49:29 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from operator import add, sub, mul, floordiv

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def evalRPN(self,  # pylint: disable=invalid-name
                tokens: list[str]) -> int:
        """Leetcode function as answer."""
        stack: deque[int] = deque()
        rpn_operators = {'+': add, '-': sub, '*': mul, '/': floordiv}
        for cur in tokens:
            if cur not in rpn_operators:
                stack.append(int(cur))
                continue
            v1, v2 = stack.pop(), stack.pop()
            res = rpn_operators[cur](v2, v1)
            if cur == "/" and res < 0 and v2 % v1 != 0:
                res += 1
            # print(v2, cur, v1, "=", res)
            stack.append(res)
        return stack.pop()


if __name__ == "__main__":
    func_timed = timer(Solution().evalRPN)
    print("result:", func_timed(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().evalRPN(
        ["2", "1", "+", "3", "*"]) == 9


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().evalRPN(
        ["4", "13", "5", "/", "+"]) == 6


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5",
         "+"]) == 22

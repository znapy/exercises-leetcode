#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Valid Parentheses.

https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/
Created on Fri Jun 14 20:38:21 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def isValid(self,  # pylint: disable=invalid-name
                s: str) -> bool:
        """Leetcode function as answer."""
        stack: deque[str] = deque()
        pair = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in "({[":
                stack.append(char)
                continue
            if not len(stack):
                return False
            if stack.pop() != pair[char]:
                return False
        return len(stack) == 0


if __name__ == "__main__":
    func_timed = timer(Solution().isValid)
    print("result:", func_timed("()[]{}"))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().isValid("()")


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().isValid("()[]{}")


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert not Solution().isValid("(]")


def test_matrieshka_different() -> None:
    assert Solution().isValid("([{}])")


def test_matrieshka_same() -> None:
    assert Solution().isValid("((()))")


def test_extra_open_bracket_1() -> None:
    assert not Solution().isValid("({)")


def test_extra_open_bracket_2() -> None:
    assert not Solution().isValid("{()")


def test_extra_open_bracket_3() -> None:
    assert not Solution().isValid("{")


def test_extra_open_bracket_4() -> None:
    assert not Solution().isValid("(){")


def test_extra_closed_bracket_1() -> None:
    assert not Solution().isValid("(})")


def test_extra_closed_bracket_2() -> None:
    assert not Solution().isValid("}()")


def test_extra_closed_bracket_3() -> None:
    assert not Solution().isValid("}")


def test_extra_closed_bracket_4() -> None:
    assert not Solution().isValid("()}")

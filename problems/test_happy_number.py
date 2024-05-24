#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Happy Number.

https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
Created on Fri May 24 14:14:30 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from typing import Callable
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def isHappy(self,  # pylint: disable=invalid-name
                n: int) -> bool:
        """Leetcode function as answer."""
        history = set()
        calc: Callable[[int], int] = lambda val: \
            sum(pow(int(char), 2) for char in str(val))
        cur = calc(n)
        while cur not in history:
            # print(cur)
            if cur == 1:
                return True
            history.add(cur)
            cur = calc(cur)
        return False


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().isHappy)
    nums = 123456789012345678901234567890
    print("result:", func_timed(nums))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().isHappy(19) is True


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().isHappy(2) is False

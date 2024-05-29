#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
First Unique Character in a String.

https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1120/
Created on Tue May 28 08:47:16 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def firstUniqChar(self,  # pylint: disable=invalid-name
                      s: str) -> int:
        """Leetcode function as answer."""
        repeated: set[str] = set()
        once: dict[str, int] = dict()
        for i, char in enumerate(s):
            if char in repeated:
                continue

            if char in once:
                repeated.add(char)
                once.pop(char)
                continue

            once[char] = i

        if not len(once):
            return -1

        result = len(s)
        for _, val in once.items():
            if val < result:
                result = val

        return result


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().firstUniqChar)
    print("result:", func_timed(["a"]*100000))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().firstUniqChar("leetcode") == 0


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().firstUniqChar("loveleetcode") == 2


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().firstUniqChar("aabb") == -1


def test_leetcode_case_dddccdbba() -> None:
    assert Solution().firstUniqChar("dddccdbba") == 8

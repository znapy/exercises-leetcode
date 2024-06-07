#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Longest Substring Without Repeating Characters.

https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1135/
Created on Tue Jun  4 08:32:03 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def lengthOfLongestSubstring(self,  # pylint: disable=invalid-name
                                 s: str) -> int:
        """Leetcode function as answer."""
        # Leetcode solution is shorter - they do not remove elements
        # from history - just update them to i if stone is higher
        # and count size from stone
        result, cur_len, stone = 0, 0, 0
        history: dict[str, int] = {}
        for j, cur in enumerate(s):
            cur_len += 1
            found = history.get(cur, None)
            if found is None:
                history[cur] = j
                continue

            result = max(result, cur_len-1)

            for i in range(stone, found+1):
                cur_len -= 1
                history.pop(s[i])
            stone = found+1
            history[cur] = j

        return max(result, cur_len)


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().lengthOfLongestSubstring)
    print("result:", func_timed("abcabcbb"))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().lengthOfLongestSubstring(
        "abcabcbb") == 3


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().lengthOfLongestSubstring(
        "bbbbb") == 1


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().lengthOfLongestSubstring(
        "pwwkew") == 3


def test_common() -> None:
    """The third example in the task."""
    func = Solution().lengthOfLongestSubstring

    assert func("") == 0

    assert func("a") == 1

    assert func("aa") == 1

    assert func(" a") == 2

    assert func(" a ") == 2

    assert func(" a ab") == 3

    assert func(" a ab ") == 3

    assert func("abab") == 2

    assert func("ababc") == 3

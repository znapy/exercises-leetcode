#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Group Anagrams.

https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1124/
Created on Fri May 31 08:11:36 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import defaultdict
from typing import Callable
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def groupAnagrams(self,  # pylint: disable=invalid-name
                      strs: list[str]) -> list[list[str]]:
        """Leetcode function as answer."""
        hash_map: defaultdict[str, list[str]] = defaultdict(list)
        get_key: Callable[[str], str] = lambda x: "".join(sorted(list(x)))
        for val in strs:
            hash_map[get_key(val)].append(val)
        return list(hash_map.values())


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().groupAnagrams)
    print("result:", func_timed(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().groupAnagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]) == \
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().groupAnagrams(
        [""]) == [[""]]


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().groupAnagrams(
        ["a"]) == [["a"]]

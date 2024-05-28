#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimum Index Sum of Two Lists.

https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/
Created on Mon May 27 08:24:08 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def findRestaurant(self,  # pylint: disable=invalid-name
                       list1: list[str], list2: list[str]) -> list[str]:
        """Leetcode function as answer."""
        dict1 = {val: key for key, val in enumerate(list1)}
        dict2 = {val: key for key, val in enumerate(list2)}
        common_strings = dict1.keys() & dict2.keys()
        least_index_sum = len(list1) + len(list2)

        result: list[str] = []
        for val in common_strings:
            cur_index_sum = dict1[val] + dict2[val]
            if cur_index_sum > least_index_sum:
                continue
            if cur_index_sum == least_index_sum:
                result.append(val)
            if cur_index_sum < least_index_sum:
                least_index_sum = cur_index_sum
                result = [val]
        return result


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().findRestaurant)
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    print("result:", func_timed(list1, list2))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse",
         "Shogun"]) == ["Shogun"]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"]) == ["Shogun"]


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    result = Solution().findRestaurant(
        ["happy", "sad", "good"], ["sad", "happy", "good"])
    assert sorted(result) == ["happy", "sad"]

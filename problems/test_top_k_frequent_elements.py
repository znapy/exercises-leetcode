#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Top K Frequent Elements.

https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1133/
Created on Fri Jun  7 08:12:02 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import Counter
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def topKFrequent(self,  # pylint: disable=invalid-name
                     nums: list[int], k: int) -> list[int]:
        """Leetcode function as answer."""
        # Leetcode solution:
        # hashmap = {}
        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num] += 1
        #     else:
        #         hashmap[num] = 1
        # heap = []
        # for key in hashmap:
        #     heapq.heappush(heap, (-hashmap[key], key))

        # res = []
        # for _ in range(k):
        #     popped = heapq.heappop(heap)
        #     res.append(popped[1])

        # return res
        return [x for x, _ in Counter(nums).most_common(k)]


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().topKFrequent)
    print("result:", func_timed([1, 1, 1, 2, 2, 3], k=2))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().topKFrequent(
        [1, 1, 1, 2, 2, 3], k=2) == [1, 2]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().topKFrequent(
        [1], k=1) == [1]

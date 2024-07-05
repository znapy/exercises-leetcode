#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find K Closest Elements.

https://leetcode.com/explore/learn/card/binary-search/135/template-iii/945/
Created on Fri Jul  5 07:36:52 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    def findClosestElements(self,  # pylint: disable=invalid-name
                            arr: list[int], k: int, x: int) -> list[int]:
        """Leetcode function as answer."""
        low, high = 0, len(arr)
        while low < high:
            mid = low + (high-low)//2
            if arr[mid] < x:
                low = mid+1
            else:
                high = mid
        low, high = low-1, low
        result: list[int] = []

        while k > 0:
            k -= 1
            if low == -1:
                result.append(arr[high])
                high = high+1
            elif high == len(arr):
                result.append(arr[low])
                low = low-1
            elif abs(arr[low] - x) > abs(arr[high] - x):
                result.append(arr[high])
                high = high+1
            else:
                result.append(arr[low])
                low = low-1

        return sorted(result)
        # Leetcode solution - in second part do not use list
        # but shift high and low pointers. The result is arr[low+1:high].
        # Another solution thrue heap:
        #     heap = []
        #     for val in arr:
        #         dist = abs(val - x)
        #         if len(heap) < k:
        #             heappush(heap, (-1 * dist, val))
        #         else:
        #             if -1 * heap[0][0] > dist:
        #                 heappop(heap)
        #                 heappush(heap, (-1 * dist, val))
        #     return sorted([val for _, val in heap])


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().findClosestElements)

    print("result:", func_timed([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().findClosestElements(
        [1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().findClosestElements(
        [1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]


def test_common() -> None:
    f = Solution().findClosestElements
    assert f([0], 1, 2) == [0]
    assert f([0], 1, -1) == [0]
    assert f([-1, 1, 3], 2, -2) == [-1, 1]
    assert f([-1, 1, 3], 2, -1) == [-1, 1]
    assert f([-1, 1, 3], 2, 0) == [-1, 1]
    assert f([-1, 1, 3], 2, 1) == [-1, 1]
    assert f([-1, 1, 3], 2, 2) == [1, 3]
    assert f([-1, 1, 3], 2, 3) == [1, 3]

    assert f([1, 3, 5, 7], 2, 0) == [1, 3]
    assert f([1, 3, 5, 7], 2, 1) == [1, 3]
    assert f([1, 3, 5, 7], 2, 2) == [1, 3]
    assert f([1, 3, 5, 7], 2, 3) == [1, 3]
    assert f([1, 3, 5, 7], 2, 4) == [3, 5]
    assert f([1, 3, 5, 7], 2, 5) == [3, 5]
    assert f([1, 3, 5, 7], 2, 6) == [5, 7]
    assert f([1, 3, 5, 7], 2, 7) == [5, 7]
    assert f([1, 3, 5, 7], 2, 8) == [5, 7]
    assert f([1, 3, 5, 7], 4, 100) == [1, 3, 5, 7]

    assert f([-3, -2, -1], 2, -4) == [-3, -2]
    assert f([-3, -2, -1], 2, -3) == [-3, -2]
    assert f([-3, -2, -1], 2, -2) == [-3, -2]
    assert f([-3, -2, -1], 2, -1) == [-2, -1]
    assert f([-3, -2, -1], 2, 0) == [-2, -1]

    # Leetcode unittest 1
    assert f(
        [0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4) ==\
        [0, 1, 1, 1, 2, 3, 6, 7, 8]
    # Leetcode unittest 2
    assert f([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5) == [3, 3, 4]

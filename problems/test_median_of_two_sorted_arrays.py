#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Median of Two Sorted Arrays.

https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1040/
Created on Thu Jul 11 12:45:38 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from bisect import bisect_left, bisect_right
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def findMedianSortedArrays(self,  # pylint: disable=invalid-name
                               nums1: list[int], nums2: list[int]) -> float:
        """Leetcode function as answer."""
        if len(nums1) > len(nums2):
            big, sml, big_l, sml_l, big_r, sml_r = \
                nums1, nums2, 0, 0, len(nums1) - 1, len(nums2) - 1
        else:
            big, sml, big_l, sml_l, big_r, sml_r = \
                nums2, nums1, 0, 0, len(nums2) - 1, len(nums1) - 1

        def point_from_range(lo: int, hi: int) -> tuple[int, int]:
            return divmod(lo + hi, 2)

        def discover() -> tuple[int, int]:
            val = big[big_m[0]]
            ip_l = bisect_left(sml, val, sml_l, sml_r+1)
            ip_r = bisect_right(sml, val, ip_l, sml_r+1)
            return (ip_l, ip_r)

        def divide() -> float | None:
            nonlocal sml_l, sml_r, big_l, big_r
            val1, big_next = big[big_m[0]], big_m[0] + 1
            sml_next, sml_next2 = discovered[0], discovered[1]
            current, current2 = big_m[0] + sml_next, big_m[0] + sml_next2

            if current2 > middle[0] and current < middle[0]:
                return float(val1)
            if current > middle[0]:
                big_r, sml_r = big_m[0] - 1, sml_next - 1
                return None
            if current2 < middle[0]:
                big_l, sml_l = big_m[0] + 1, sml_next2
                return None

            if current == middle[0] or current2 == middle[0]:

                if middle[1] == 0:
                    return float(val1)

                corners = []
                if big_next < len(big):
                    corners.append(big[big_next])
                if current == middle[0]:
                    if sml_next < len(sml):
                        corners.append(sml[sml_next])
                    return (val1 + min(corners)) / 2
                if current2 == middle[0]:
                    if sml_next2 < len(sml):
                        corners.append(sml[sml_next2])
                    return (val1 + min(corners)) / 2

            raise ValueError

        middle = point_from_range(0, sml_r + big_r + 1)
        while True:
            big_m = point_from_range(big_l, big_r)
            discovered = discover()
            result = divide()  # change *_l + *_r points
            if result is not None:
                return result
            if (big_r - big_l) <= (sml_r - sml_l):
                big, sml = sml, big
                big_l, big_r, sml_l, sml_r = sml_l, sml_r, big_l, big_r

    @staticmethod
    def _lcs(nums1: list[int], nums2: list[int]) -> float:
        """Leetcode solution"""
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) // 2
        i = bisect_left(range(m), True,
                        key=lambda i: after-i-1 < 0 or a[i] >= b[after-i-1])
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
        return (nextfew[0] + nextfew[1 - (m+n) % 2]) / 2.0


def main() -> None:
    """Start point."""
    nums1 = list(range(1, 1000))
    nums2 = list([1]*10 + [2]*10 + [3]*10 + [4]*70)
    func_timed = timer(Solution().findMedianSortedArrays)
    print("result 1:", func_timed(nums1, nums2))
    print("result 2:", timer(Solution._lcs)(nums1, nums2))


if __name__ == "__main__":
    main()

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().findMedianSortedArrays(
        [1, 3], [2]) == 2.0


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().findMedianSortedArrays(
        [1, 2], [3, 4]) == 2.5


def test_common() -> None:
    func = Solution().findMedianSortedArrays

    assert func([1], []) == 1.0
    assert func([1, 2], []) == 1.5
    assert func([-1, -2], []) == -1.5
    assert func([1, 2, 4], [3, 5]) == 3.0

    assert func([1, 3], [0]) == 1.0
    assert func([1, 3], [1]) == 1.0
    assert func([1, 3], [2]) == 2.0
    assert func([1, 3], [3]) == 3.0
    assert func([1, 3], [4]) == 3.0
    assert func([-3, -1], [0]) == -1.0
    assert func([-3, -1], [-1]) == -1.0
    assert func([-3, -1], [-2]) == -2.0
    assert func([-3, -1], [-3]) == -3.0
    assert func([-3, -1], [-4]) == -3.0

    assert func([3, 6], [1, 1]) == 2.0
    assert func([3, 6], [1, 2]) == 2.5
    assert func([3, 6], [1, 3]) == 3.0
    assert func([3, 6], [1, 4]) == 3.5
    assert func([3, 6], [1, 5]) == 4.0
    assert func([3, 6], [1, 6]) == 4.5
    assert func([3, 6], [1, 7]) == 4.5

    assert func([3, 6, 9], [3]) == 4.5
    assert func([3, 6, 9], [4]) == 5.0
    assert func([3, 6, 9], [6]) == 6.0
    assert func([3, 6, 9], [7]) == 6.5
    assert func([3, 6, 9], [9]) == 7.5
    assert func([3, 6, 9], [10]) == 7.5

    assert func([1, 2, 3, 4], [5, 6, 7, 8]) == 4.5
    assert func([1, 3, 5, 7], [2, 4, 6, 8]) == 4.5
    assert func([2, 4, 6, 8], [1, 3, 5, 7]) == 4.5
    assert func([5, 6, 7, 8], [1, 2, 3, 4]) == 4.5

    # Leetcode unittest 1
    assert func([1], [2, 3, 4]) == 2.5

    # Leetcode unittest 2
    assert func([1, 3, 4], [2, 5, 6]) == 3.5

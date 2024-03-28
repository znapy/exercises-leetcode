#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arrays 101: Remove Duplicates from Sorted Array.

https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
Created on Tue Mar 26 09:13:31 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class Solution:
    """Leetcode class for answers."""

    @timer
    def remove_duplicates_brute(self, nums: list[int]) -> int:
        """Remove duplicates - simpliest."""
        nums[:] = sorted(list(set(nums)))

        return len(nums)

    def removeDuplicates(self,  # pylint: disable=invalid-name
                         nums: list[int]) -> int:
        """Remove duplicates."""
        length = len(nums)
        if length < 2:
            return length
        j = 1
        for i in range(length):

            while j < length \
              and nums[i] == nums[j]:

                j += 1

            if j == length:
                break

            nums[i + 1] = nums[j]
            j += 1

        return i + 1


if __name__ == "__main__":
    remove_timed = timer(Solution().removeDuplicates)
    nums = [0, 1, 1, 2, 3, 4, 5]
    print("result:", remove_timed(nums), nums)

    nums = [0, 1, 1, 2, 3, 4, 5]
    print("result:", Solution().remove_duplicates_brute(nums), nums)


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    nums = [1, 1, 2]
    result = Solution().removeDuplicates(nums)
    assert result == 2
    assert nums[:result] == [1, 2]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = Solution().removeDuplicates(nums)
    assert result == 5
    assert nums[:result] == [0, 1, 2, 3, 4]


def test_0() -> None:
    nums = [0]
    result = Solution().removeDuplicates(nums)
    assert result == 1
    assert nums[:result] == [0]


def test_minus_1_1() -> None:
    nums = [-1, 1]
    result = Solution().removeDuplicates(nums)
    assert result == 2
    assert nums[:result] == [-1, 1]


def test_1_2_2() -> None:
    nums = [1, 2, 2]
    result = Solution().removeDuplicates(nums)
    assert result == 2
    assert nums[:result] == [1, 2]


def test_minuses_10_9_9_10() -> None:
    nums = [-10, -9, -9, 10]
    result = Solution().removeDuplicates(nums)
    assert result == 3
    assert nums[:result] == [-10, -9, 10]

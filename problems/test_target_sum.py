#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target Sum.

https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1389/
Created on Tue Jun 18 07:09:02 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from timer import timer


class Solution:
    """Leetcode class for answers."""

    def findTargetSumWays(self,  # pylint: disable=invalid-name
                          nums: list[int], target: int) -> int:
        """Leetcode function as answer."""
        result, length = 0, len(nums)

        # Variant 1 - time is too long due to format string (guess)
        #   timer: 2.94733787 seconds in "Leetcode unittest 2"
        # for binary representation, 0 as "-" and 1 as "+"
        # pattern = '{fill}{width}b'.format(width=length, fill=0)
        # for step in range(2 ** length):
        #     cur, signs = 0, format(step, pattern)
        #     for i in range(length):
        #         cur += nums[i] if signs[i] == "1" else -nums[i]
        #     if cur == target:
        #         result += 1

        # Variant 2 - time is too long due to count previous value again:
        #   timer: 3.16887379 seconds in "Leetcode unittest 2"
        # signs, next_step = [0] * length, True
        # while next_step:
        #     next_step, cur = False, 0
        #     for i in range(length):
        #         cur += nums[i] if signs[-i] == 1 else -nums[i]
        #         if next_step:
        #             continue
        #         if signs[-i] == 0:
        #             signs[-i] = 1
        #             next_step = True
        #         else:
        #             signs[-i] = 0
        #     if cur == target:
        #         result += 1

        # Variant 3 - using stack of sums, 3-times faster, but still slow:
        #   55 / 140 test cases passed. Status: Time Limit Exceeded
        #   timer: 0.92415118 seconds in "Leetcode unittest 2"
        # stack = deque([("+", nums[0])])
        # while stack:
        #     seq_number = len(stack)
        #     if seq_number < length:
        #         sign, sums = stack[-1]
        #         stack.append(("+", sums + nums[seq_number]))
        #         continue

        #     sign, sums = stack.pop()
        #     if sums == target:
        #         result += 1
        #     while sign == "-" and (seq_number := len(stack)):
        #         sign, sums = stack.pop()
        #     if seq_number:
        #         stack.append(("-", sums - nums[seq_number-1]*2))

        # Variant 4 - using stack and list of sums
        #   - bad time (1.75527835 seconds)
        # stack = deque(zip(nums, accumulate(nums)))
        # prev_checks: List[Tuple[str, int]] = []
        # first = True
        # while stack:
        #     cur_num, _ = stack.pop()

        #     checks: List[Tuple[str, int]] = []

        #     if not prev_checks:
        #         checks.append(("+" + str(cur_num), cur_num))
        #         checks.append(("-" + str(cur_num), -cur_num))

        #     for right_key, right_minsum in prev_checks:
        #         key = f"{str(cur_num)}, {right_key}"
        #         checks.append(("+" + key, cur_num + right_minsum))
        #         checks.append(("-" + key, -cur_num + right_minsum))

        #     prev_checks = []
        #     for key, val in checks:
        #         prev_checks.append((key, val))
        #         if not first and key[0] == "+":
        #             continue
        #         left_sum = 0
        #         if stack:
        #             left_sum = stack[-1][1]
        #         if left_sum + val == target:
        #             result += 1

        #     first = False

        # Variant 5 - using sublist of sums
        #   0.06212521 seconds in "Leetcode unittest 2"
        def leaves(nums: list[int]) -> deque[int]:
            """My function to get leaves in findTargetSumWays."""
            prevs = deque([0])
            for num in nums:
                counter = len(prevs)
                while counter:
                    counter -= 1
                    prev = prevs.popleft()
                    prevs.append(prev + num)
                    prevs.append(prev - num)
            return prevs

        if length == 1:
            for val in leaves(nums):
                if val == target:
                    result += 1
            return result

        mid = length // 2
        heads = leaves(nums[:mid])
        tails = leaves(nums[mid:])
        for h in heads:
            for t in tails:
                if h + t == target:
                    result += 1
        return result

        # Variant 6 - leetcode solution
        #   0.00813627 seconds in "Leetcode unittest 2"
        # count = Counter({0: 1})
        # for x in nums:
        #     step = Counter()
        #     for y in count:
        #         step[y + x] += count[y]
        #         step[y - x] += count[y]
        #     count = step
        # return count[target]


if __name__ == "__main__":
    func_timed = timer(Solution().findTargetSumWays)
    print("result:", func_timed(
        [42, 36, 4, 15, 17, 15, 31, 1, 11, 2, 12, 28, 22, 9, 2, 31,
         48, 18, 48, 5], 15))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().findTargetSumWays([1], 1) == 1


def test_my() -> None:
    func = Solution().findTargetSumWays
    assert func([0], 1) == 0
    assert func([0], 0) == 2
    assert func([0, 0], 1) == 0
    assert func([0, 0], 0) == 4
    assert func([0, 0, 0], 0) == 8

    assert func([1], -1) == 1
    assert func([1, 1], -1) == 0
    assert func([1, 1, 1], -1) == 3
    assert func([1, 1, 1], 1) == 3


def test_leetcode_unittest_1() -> None:
    assert Solution().findTargetSumWays(
        [2, 20, 24, 38, 44, 21, 45, 48, 30, 48, 14, 9, 21, 10, 46, 46, 12, 48,
         12, 38], 48) == 5401


def test_leetcode_unittest_2() -> None:
    assert Solution().findTargetSumWays(
        [42, 36, 4, 15, 17, 15, 31, 1, 11, 2, 12, 28, 22, 9, 2, 31, 48, 18, 48,
         5], 15) == 7219

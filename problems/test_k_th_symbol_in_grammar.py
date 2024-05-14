#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
K-th Symbol in Grammar.

https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/1675/
Created on Mon May 13 15:21:16 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from sys import getsizeof

from timer import timer


class ClassNode:
    """Definition for singly-linked list."""

    __slots__ = ['val', 'next_']

    def __init__(self, x: int) -> None:
        self.val = x
        self.next_: ClassNode | None = None


class Solution:
    """Leetcode class for answers."""

    # A lot of classes takes more memory than list of values
    def kthGrammar_linked_list(self,  # pylint: disable=invalid-name
                               n: int, k: int) -> int:
        """Leetcode function as answer."""
        head = tail = point = corner = ClassNode(0)
        for _ in range(1, k):
            tail.next_ = ClassNode(0 if point.val else 1)
            tail = tail.next_

            if point == corner:
                point = head
                corner = tail
            else:
                point = point.next_  # type: ignore[assignment]
        return tail.val

    # List takes more memory than bytearray
    def kthGrammar_array(self,  # pylint: disable=invalid-name
                         n: int, k: int) -> int:
        """Leetcode function as answer."""
        sequence = [0] * k
        slow, corner = 0, 1
        for fast in range(1, k):
            slow += 1
            if slow == corner:
                slow = 0
                corner = fast

            if sequence[slow] == 0:
                sequence[fast] = 1
        return sequence[-1]

    # Still not good - memory limit exceeded in parameters: (30, 434991989)
    def kthGrammar_bytearray(self,  # pylint: disable=invalid-name
                             n: int, k: int) -> int:
        """Leetcode function as answer."""
        sequence = bytearray(k)
        slow, corner = 0, 1
        for fast in range(1, k):
            slow += 1
            if slow == corner:
                slow = 0
                corner = fast

            if sequence[slow] == 0:
                sequence[fast] = 1
        return sequence[-1]

    def kthGrammar(self,  # pylint: disable=invalid-name
                   n: int, k: int) -> int:
        """Leetcode function as answer."""
        return bin(k - 1).count('1') & 1


if __name__ == "__main__":
    size_node = getsizeof(ClassNode(0))
    print("size of nodes:", size_node, size_node*2, size_node*4)
    print("size of list:", getsizeof([0]), getsizeof([0, 1]),
          getsizeof([0, 1, 1, 0]))  # Boolean is the same as int
    print("size of bytearray:", getsizeof(bytearray(1)),
          getsizeof(bytearray(2)), getsizeof(bytearray(4)))
    print("size of bin:", getsizeof(bin(0)), getsizeof(bin(1)),
          getsizeof(bin(6)))  # the leading "0" we can imagine :)
    s = Solution()
    funcs = (s.kthGrammar_linked_list,
             s.kthGrammar_array,
             s.kthGrammar_bytearray,
             s.kthGrammar)
    for func in funcs:
        print("result:", timer(func)(
            30, 10_000_000))

    # result = ""
    # for x in range(1, 257):
    #     result += str(func(9, x))
    # print(result)
    # Values in first lines
    # 0
    # 01
    # 0110
    # 01101001
    # 0110100110010110
    # 01101001100101101001011001101001
    # 0110100110010110100101100110100110010110011010010110100110010110
    # 01101001100101101001011001101001100101100110100101101001100101101001011001101001011010011001011001101001100101101001011001101001
    # 0110100110010110100101100110100110010110011010010110100110010110100101100110100101101001100101100110100110010110100101100110100110010110011010010110100110010110011010011001011010010110011010010110100110010110100101100110100110010110011010010110100110010110


#########
# Tests
# pylint: disable=missing-function-docstring


# float result needs to be rounded up,
# but I'm too lazy - it works like this :)
def test_leetcode_example_1() -> None:
    """The first example in the task."""
    assert Solution().kthGrammar(
        3, 4) == 0


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().kthGrammar(
        2, 1) == 0


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().kthGrammar(
        2, 2) == 1


def test_3() -> None:
    assert Solution().kthGrammar(
        3, 3) == 1


def test_4() -> None:
    assert Solution().kthGrammar(
        3, 4) == 0


def test_5() -> None:
    assert Solution().kthGrammar(
        4, 5) == 1


def test_6() -> None:
    assert Solution().kthGrammar(
        4, 6) == 0


def test_7() -> None:
    assert Solution().kthGrammar(
        4, 7) == 0


def test_8() -> None:
    assert Solution().kthGrammar(
        4, 8) == 1


def test_x() -> None:
    func = Solution().kthGrammar
    result = ""
    for x in range(1, 33):
        result += str(func(6, x))
    assert result == "01101001100101101001011001101001"

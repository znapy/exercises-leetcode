#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design HashSet.

https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1139/
Created on Tue Mar 26 09:13:31 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from typing import Callable

from timer import timer


class MyHashSet:
    """
    My implement MyHashSet class.

    Leetcode solution is the same.
    One man think about situation if it will be a lot of keys - more,
    than memory - he used List for hash size 10000. The List contains
    a ListNodes (key and next point) for every key in collision. Also
    he proposed to use red-black tree if we will write much more than
    read.
    """

    SIZE = 1000001

    def __init__(self) -> None:
        self.values: list[bool] = [False] * self.SIZE
        self.hash: Callable[[int], int] = lambda x: x % self.SIZE

    def add(self, key: int) -> None:
        """Insert the value key into the HashSet."""
        self.values[self.hash(key)] = True

    def remove(self, key: int) -> None:
        """
        Remove the value key in the HashSet.

        If key does not exist in the HashSet, do nothing.
        """
        self.values[self.hash(key)] = False

    def contains(self, key: int) -> bool:
        """Return whether the value key exists in the HashSet or not."""
        return self.values[self.hash(key)]


def main() -> None:
    """Start point."""
    hash_set = MyHashSet()
    timer(hash_set.add)(1)
    timer(hash_set.add)(2)
    print("is it contains 1:", timer(hash_set.contains)(1))
    print("is it contains 3:", timer(hash_set.contains)(3))
    timer(hash_set.add)(2)
    print("is it contains 2:", timer(hash_set.contains)(2))
    timer(hash_set.remove)(2)
    print("is it contains 2:", timer(hash_set.contains)(2))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    hash_set = MyHashSet()
    hash_set.add(1)
    hash_set.add(2)
    assert hash_set.contains(1) is True
    assert hash_set.contains(3) is False
    hash_set.add(2)
    assert hash_set.contains(2) is True
    hash_set.remove(2)
    assert hash_set.contains(2) is False

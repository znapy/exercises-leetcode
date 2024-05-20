#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design HashMap.

https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1140/
Created on Sun May 19 14:13:14 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from typing import Callable

from timer import timer


class MyHashMap:
    """My implement MyHashMap class."""

    SIZE = 1000001

    def __init__(self) -> None:
        self.values: list[int] = [-1] * self.SIZE
        self.hash: Callable[[int], int] = lambda x: x % self.SIZE

    def put(self, key: int, value: int) -> None:
        """
        Insert a (key, value) pair into the HashMap.

        If the key already exists in the map, update the corresponding value.
        """
        self.values[self.hash(key)] = value

    def get(self, key: int) -> int:
        """
        Return the value to which the specified key is mapped.

        Return -1 if this map contains no mapping for the key.
        """
        return self.values[self.hash(key)]

    def remove(self, key: int) -> None:
        """
        Remove the key and its corresponding value.

        If the map contains the mapping for the key.
        """
        self.values[self.hash(key)] = -1


def main() -> None:
    """Start point."""
    hash_map = MyHashMap()
    timer(hash_map.put)(1, 1)
    timer(hash_map.put)(2, 2)
    print("is it contains 1:", timer(hash_map.get)(1))
    print("is it contains 3:", timer(hash_map.get)(3))
    timer(hash_map.put)(2, 1)
    print("is it contains 2:", timer(hash_map.get)(2))
    timer(hash_map.remove)(2)
    print("is it contains 2:", timer(hash_map.get)(2))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    hash_map = MyHashMap()
    hash_map.put(1, 1)
    hash_map.put(2, 2)
    assert hash_map.get(1) == 1
    assert hash_map.get(3) == -1
    hash_map.put(2, 1)
    assert hash_map.get(2) == 1
    hash_map.remove(2)
    assert hash_map.get(2) == -1

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Insert Delete GetRandom O(1).

https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1141/
Created on Sun Jun  9 08:44:00 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from random import randrange
from timer import timer


class RandomizedSet:
    """Leetcode class for answers."""
    # Leetcode solution - have additional dict to remember indexes of values.
    # In remove operation in List - swap removed and last value, then remove
    # the last value.

    def __init__(self) -> None:
        self.vals: list[int] = []

    def insert(self, val: int) -> bool:
        """
        Inserts an item val into the set if not present.

        Returns true if the item was not present, false otherwise.
        """
        if val in self.vals:
            return False
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes an item val from the set if present.

        Returns true if the item was present, false otherwise.
        """
        if val in self.vals:
            self.vals.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Returns a random element from the current set of elements.

        It's guaranteed that at least one element exists when this method
        is called.
        Each element must have the same probability of being returned.
        """
        return self.vals[randrange(len(self.vals))]


def main() -> None:
    """Start point."""
    rs = RandomizedSet()

    print(timer(rs.insert)(1)) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    print(timer(rs.remove)(2)) # Returns false as 2 does not exist in the set.
    print(timer(rs.insert)(2)) # Inserts 2 to the set, returns true. Set now contains [1,2].
    print(timer(rs.getRandom)()) # getRandom() should return either 1 or 2 randomly.
    print(timer(rs.remove)(1)) # Removes 1 from the set, returns true. Set now contains [2].
    print(timer(rs.insert)(2)) # 2 was already in the set, so return false.
    print(timer(rs.getRandom)()) # Since 2 is the only number in the set, getRandom() will always return 2.


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    rs = RandomizedSet()

    assert rs.insert(1) is True
    assert rs.remove(2) is False
    assert rs.insert(2) is True
    assert rs.getRandom() in (1, 2)
    assert rs.remove(1) is True
    assert rs.insert(2) is False
    assert rs.getRandom() == 2

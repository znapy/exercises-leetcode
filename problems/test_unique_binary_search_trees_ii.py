#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unique Binary Search Trees II.

https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2384/
Created on Tue May 14 08:03:08 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from itertools import permutations

from timer import timer


class TreeNode:
    """Definition for a binary tree node."""

    __slots__ = ['val', 'left', 'right']

    def __init__(self, val: int = 0, left: ['TreeNode', None] = None,
                 right: ['TreeNode', None] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BST:
    """My constructor for binary search tree."""

    def __init__(self, head: TreeNode) -> None:
        self.head = head

    def add(self, node: TreeNode) -> None:
        """Add new node to BST with standart rules."""
        cur = self.head
        while True:
            if node.val < cur.val:
                if cur.left is None:
                    cur.left = node
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    break
                cur = cur.right

    def __repr__(self) -> str:
        queue: deque[TreeNode | None] = deque([self.head])
        result, counter = "", 1
        while counter:
            current = queue.popleft()
            if current is None:
                result += ",None"
                # queue.extend([None, None])
                continue
            counter -= 1
            result += f",{current.val}"
            queue.append(current.left)
            if current.left:
                counter += 1
            queue.append(current.right)
            if current.right:
                counter += 1

        return "<TreeNode: [" + result[1:] + "]>"


class Solution:
    """Leetcode class for answers."""

    def generateTrees(self,  # pylint: disable=invalid-name
                      n: int) -> list[TreeNode]:
        """Leetcode function as answer."""
        result: dict[str, TreeNode] = {}
        # Brute: add everithing, filter in dict
        for vals in permutations(range(1, n + 1)):
            bst = BST(TreeNode(vals[0]))
            for val in vals[1:]:
                bst.add(TreeNode(val))
            result[str(bst)] = bst.head

        return list(result.values())


if __name__ == "__main__":
    print("timing Solution for n=8:")
    result1 = timer(Solution().generateTrees)(4)
    print("length is:", len(result1))


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    trees = Solution().generateTrees(3)

    assert len(trees) == 5

    # (1, 2, 3)
    assert trees[0].val == 1
    assert trees[0].left is None
    assert trees[0].right.val == 2
    assert trees[0].right.left is None
    assert trees[0].right.right.val == 3
    assert trees[0].right.right.left is None
    assert trees[0].right.right.right is None

    # (1, 3, 2)
    assert trees[1].val == 1
    assert trees[1].left is None
    assert trees[1].right.val == 3
    assert trees[1].right.left.val == 2
    assert trees[1].right.right is None
    assert trees[1].right.left.left is None
    assert trees[1].right.left.right is None

    # (2, 1, 3) = (2, 3, 1)
    assert trees[2].val == 2
    assert trees[2].left.val == 1
    assert trees[2].right.val == 3
    assert trees[2].left.left is None
    assert trees[2].left.right is None
    assert trees[2].right.left is None
    assert trees[2].right.right is None

    # (3, 1, 2)
    assert trees[3].val == 3
    assert trees[3].left.val == 1
    assert trees[3].right is None
    assert trees[3].left.left is None
    assert trees[3].left.right.val == 2
    assert trees[3].left.right.left is None
    assert trees[3].left.right.right is None

    # (3, 2, 1)
    assert trees[4].val == 3
    assert trees[4].left.val == 2
    assert trees[4].right is None
    assert trees[4].left.left.val == 1
    assert trees[4].left.right is None
    assert trees[4].left.left.left is None
    assert trees[4].left.left.right is None


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    trees = Solution().generateTrees(1)
    assert len(trees) == 1
    assert trees[0].val == 1
    assert trees[0].left is None
    assert trees[0].right is None


def test_4() -> None:
    trees = Solution().generateTrees(4)
    assert len(trees) == 14
    assert str(BST(trees[0])) == "<TreeNode: [1,None,2,None,3,None,4]>"

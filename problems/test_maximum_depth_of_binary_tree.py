#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Maximum Depth of Binary Tree.

https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2375/
Created on Sat May 11 08:52:07 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from functools import lru_cache
from collections import deque

from timer import timer


class TreeNode:
    """Leetcode definition for a binary tree node."""

    def __init__(self, val: int = 0, left: ["TreeNode", None] = None,
                 right: ["TreeNode", None] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def construct(vals: list[int | None]) -> "TreeNode":
        """My realisation - construct the Tree from a list."""
        if not len(vals) or type(vals[0]) is not int:
            raise ValueError("Incorrect first value in a list")
        head = TreeNode(vals[0])
        my_tree: list[TreeNode | None] = [head]
        for i, val in enumerate(vals):
            if i == 0:
                continue
            parent_idx, is_right = divmod(i - 1, 2)
            node = None if val is None else TreeNode(val)
            my_tree.append(node)
            if val is None:
                continue

            parent = my_tree[parent_idx]
            if parent is None:
                raise ValueError(f"Incorrect parent for index {i}")
            if is_right:
                parent.right = node
            else:
                parent.left = node
        return head

    def __repr__(self) -> str:
        """
        The values of each row of the tree.

        Example: [head, head.left, head.right, head.left.left, ...]
        """
        queue: deque[TreeNode | None] = deque([self])
        result, counter = "", 1
        while counter:
            current = queue.popleft()
            if current is None:
                result += ",None"
                queue.extend([None, None])
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

    def maxDepth(self,  # pylint: disable=invalid-name
                 root: TreeNode | None) -> int:
        """Leetcode function as answer."""
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        max_depth = Solution().maxDepth

        return max(max_depth(root.left), max_depth(root.right)) + 1


if __name__ == "__main__":
    func_timed = timer(Solution().maxDepth)
    print("result:", func_timed(TreeNode.construct([
        1,
        None,                   2,
        None,       None,       3,    None,
        None, None, None, None, 4, 5, None, None])))

#########
# Tests
# pylint: disable=missing-function-docstring


class TestTreeNode:

    @staticmethod
    def test_construct() -> None:
        vals = [1,
                None,                   2,
                None,       None,       3,    None,
                None, None, None, None, 4, 5, None, None]
        assert str(TreeNode.construct(vals)) == \
            "<TreeNode: [1,None,2,None,None,3,None,None,None,None,None,4,5]>"


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    head = TreeNode.construct([3, 9, 20, None, None, 15, 7])
    assert Solution().maxDepth(head) == 3


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    head = TreeNode.construct([1, None, 2])
    assert Solution().maxDepth(head) == 2


def test_None() -> None:
    assert Solution().maxDepth(None) == 0


def test_1() -> None:
    assert Solution().maxDepth(TreeNode(1)) == 1


def test_2() -> None:
    head = TreeNode.construct([1, 2])
    assert Solution().maxDepth(head) == 2


def test_3() -> None:
    vals = [1,
            None,                   2,
            None,       None,       3,    None,
            None, None, None, None, 4, 5, None, None]
    assert Solution().maxDepth(
        TreeNode.construct(vals)) == 4

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Search in a Binary Search Tree.

https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/
Created on Fri May 17 08:36:25 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from collections import deque

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

    @staticmethod
    def show_tree(tree: TreeNode) -> str:
        """Show tree as a string."""
        queue: deque[TreeNode | None] = deque([tree])
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

    def __repr__(self) -> str:
        return BST.show_tree(self.head)


class Solution:
    """Leetcode class for answers."""

    def searchBST(self,  # pylint: disable=invalid-name
                  root: TreeNode | None, val: int) -> TreeNode | None:
        """
        Search in a Binary Search Tree.

        https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/
        """
        if root is None:
            return None
        if root.val == val:
            return root
        left = None
        if root.left:
            left = self.searchBST(root.left, val)
        if left:
            return left
        right = None
        if root.right:
            right = self.searchBST(root.right, val)
        return right


if __name__ == "__main__":
    bst = BST(TreeNode(0))
    for value in range(1, 10):
        bst.add(TreeNode(value))
    found = timer(Solution().searchBST)(bst.head, 9)
    print("result:", BST.show_tree(found))


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    n1, n3 = TreeNode(1), TreeNode(3)
    n2, n7 = TreeNode(2, n1, n3), TreeNode(7)
    root = TreeNode(4, n2, n7)

    assert Solution().searchBST(root, 2) == n2


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    n1, n3 = TreeNode(1), TreeNode(3)
    n2, n7 = TreeNode(2, n1, n3), TreeNode(7)
    root = TreeNode(4, n2, n7)

    assert Solution().searchBST(root, 5) is None


def test_leetcode_testcase_1() -> None:
    n84 = TreeNode(84)
    n63 = TreeNode(63, None, n84)
    n2, n22 = TreeNode(2), TreeNode(22, None, n63)
    root = TreeNode(18, n2, n22)
    assert Solution().searchBST(root, 63) == n63

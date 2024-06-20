#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Binary Tree Inorder Traversal.

https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1383/
Created on Wed Jun 19 08:44:39 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer


class TreeNode:
    """Leetcodes class for findDuplicateSubtrees."""

    def __init__(self, val: int = 0, left: ['TreeNode', None] = None,
                 right: ['TreeNode', None] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Represint node recursevely as val,val_left,val_right."""
        stack: list[TreeNode | None] = [self]
        result: list[str] = []
        while len(stack):
            cur = stack.pop(0)
            if cur:
                result.append(str(cur.val))
                stack.append(cur.left)
                stack.append(cur.right)
            else:
                result.append('None')

        return "<TreeNode: [" + (",".join(result)) + "]>"

    @staticmethod
    def construct(nums: list[int | None]) -> list[['TreeNode', None]]:
        """Construct tree from list and return the nodes from root."""
        val = nums[0]
        if val is None:
            raise ValueError('root should be non empty')
        root = TreeNode(val)
        queue = [root]
        result: list[TreeNode | None] = [root]

        left = False
        for val in nums[1:]:
            left = not left
            parent = queue[0] if left else queue.pop(0)
            if val is None:
                result.append(None)
                continue
            cur = TreeNode(val)
            result.append(cur)
            if left:
                parent.left = cur
            else:
                parent.right = cur
            queue.append(cur)
            # print(f"for {val} (left: {left}) parant is {parent.val}")

        return result


class Solution:
    """Leetcode class for answers."""

    def inorderTraversal(self,  # pylint: disable=invalid-name
                         root: TreeNode | None) -> list[int]:
        """Leetcode function as answer."""
        return Solution().inorderTraversal(root.left) \
            + [root.val] \
            + Solution().inorderTraversal(root.right) \
            if root else []


if __name__ == "__main__":
    nodes = TreeNode.construct(list(range(100)))
    func_timed = timer(Solution().inorderTraversal)
    print("result:", func_timed(nodes[0]))

#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    nodes = TreeNode.construct([1, None, 2, 3])
    assert Solution().inorderTraversal(nodes[0]) == [1, 3, 2]


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    assert Solution().inorderTraversal(None) == []


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    assert Solution().inorderTraversal(TreeNode(1)) == [1]


def test_my() -> None:
    nodes = TreeNode.construct(list(range(1, 6)))
    assert Solution().inorderTraversal(nodes[0]) == [4, 2, 5, 1, 3]

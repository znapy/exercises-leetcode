#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find Duplicate Subtrees.

https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1127/
Created on Mon Jun  3 08:51:43 2024
@author: znapy
SPDX-License-Identifier: Apache-2.0
"""

from timer import timer
from collections import defaultdict


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
        """Construct tree from list and return the root."""
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

    def findDuplicateSubtrees(self,  # pylint: disable=invalid-name
                              root: TreeNode) -> list[TreeNode | None]:
        """Leetcode function as answer."""
        stack: list[TreeNode] = [root]
        parents: dict[TreeNode, TreeNode] = {}
        KeyNode = tuple[int | None, ...]
        candidates: defaultdict[KeyNode, set[TreeNode]] = defaultdict(set)
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
                parents[node.left] = node
            if node.right:
                stack.append(node.right)
                parents[node.right] = node
            if node.left is None and node.right is None:
                candidates[(node.val, None, None)].add(node)

        result: dict[KeyNode, TreeNode] = {}

        keys_for_parent: dict[TreeNode, KeyNode] = {}
        while candidates:
            prev, candidates = candidates, defaultdict(set)
            for key, nodes in prev.items():
                if len(nodes) == 1:
                    continue

                for node in nodes:
                    result[key] = node
                    parent = parents.get(node, None)
                    if parent is None:
                        continue

                    second_child_key: KeyNode = (None,)

                    if parent.left and parent.right:
                        second_child_key = keys_for_parent.pop(parent, (None,))
                        if second_child_key == (None,):
                            keys_for_parent[parent] = key
                            continue

                    if parent.left == node:
                        key_l, key_r = key, second_child_key
                    if parent.right == node:
                        key_r, key_l = key, second_child_key

                    parent_key = (parent.val,) + key_l + key_r
                    candidates[parent_key].add(parent)

        return list(result.values())


def main() -> None:
    """Start point."""
    func_timed = timer(Solution().findDuplicateSubtrees)
    vals = [97, 96, 96, None, None, None, 97]
    t1 = TreeNode.construct(vals)
    t2 = TreeNode.construct(vals)
    head = TreeNode(0, t1[0], t2[0])
    print("result:", func_timed(head))


if __name__ == "__main__":
    main()


#########
# Tests
# pylint: disable=missing-function-docstring


def test_leetcode_example_1() -> None:
    """The first example in the task."""
    t = TreeNode.construct([1, 2, 3, 4, None, 2, 4, None, None, 4])
    res = Solution().findDuplicateSubtrees(t[0])
    assert len(res) == 2
    assert str(res[0]) == str(t[3])
    assert str(res[1]) == str(t[1])


def test_leetcode_example_2() -> None:
    """The second example in the task."""
    t = TreeNode.construct([2, 1, 1])
    res = Solution().findDuplicateSubtrees(t[0])
    assert len(res) == 1
    assert str(res[0]) == str(t[1])


def test_leetcode_example_3() -> None:
    """The third example in the task."""
    t = TreeNode.construct([2, 2, 2, 3, None, 3, None])
    res = Solution().findDuplicateSubtrees(t[0])
    assert len(res) == 2
    assert str(res[0]) == str(t[3])
    assert str(res[1]) == str(t[1])


def test_commonn() -> None:
    """The third example in the task."""
    func = Solution().findDuplicateSubtrees

    # Leetcode unittest 1
    t = TreeNode.construct([0, 0, 0, 0, None, None, 0, None,
                           None, None, 0])
    res = func(t[0])
    assert len(res) == 1
    assert str(res[0]) == str(t[10])

    # Leetcode unittest 2
    t = TreeNode.construct([1, 2, 3, 4, 3, 2, 4, None, None, 12, 4, 4,
                           None, 31, None, None, None, None, None,
                           None, None, 2, 4])
    res = func(t[0])
    assert len(res) == 1
    assert str(res[0]) == str(t[22])

    t = TreeNode.construct([1, 2, 3, 1, None, 1, None, 2, 3, 2, 3])
    res = func(t[0])
    assert len(res) == 3
    assert str(res[0]) == str(t[7])
    assert str(res[1]) == str(t[8])
    assert str(res[2]) == str(t[3])

    t = TreeNode.construct([1, 1, 1, 1, None, 1, None, 1, 1, 1, 1])
    res = func(t[0])
    assert len(res) == 3
    assert str(res[0]) == str(t[7])
    assert str(res[1]) == str(t[3])
    assert str(res[2]) == str(t[1])

    # Leetcode unittest 3
    vals = [97, 96, 96, None, None, None, 97]
    t1 = TreeNode.construct(vals)
    t2 = TreeNode.construct(vals)
    head = TreeNode(0, t1[0], t2[0])
    res = func(head)
    assert len(res) == 4
    assert str(res[0]) == str(t1[1])
    assert str(res[1]) == str(t1[6])
    assert str(res[2]) == str(t1[2])
    assert str(res[3]) == str(t1[0])

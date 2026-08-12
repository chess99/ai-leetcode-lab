# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getNumber(self, root: Optional['TreeNode'], ops: List[List[int]]) -> int:
        values = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            values.append(node.val)
            node = node.right

        parent = list(range(len(values) + 1))

        def find(index: int) -> int:
            while parent[index] != index:
                parent[index] = parent[parent[index]]
                index = parent[index]
            return index

        red = 0
        # 逆序处理：每个节点最终颜色由最后一次覆盖它的操作决定。
        from bisect import bisect_left, bisect_right
        for color, left, right in reversed(ops):
            index = find(bisect_left(values, left))
            end = bisect_right(values, right)
            while index < end:
                red += color
                parent[index] = find(index + 1)
                index = parent[index]
        return red

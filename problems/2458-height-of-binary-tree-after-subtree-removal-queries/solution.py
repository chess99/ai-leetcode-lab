# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
try:
    TreeNode
except NameError:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                height[node] = 1 + max(height.get(node.left, -1),
                                       height.get(node.right, -1))
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        answer = {root.val: 0}
        stack = [(root, 0, 0)]
        while stack:
            node, depth, outside = stack.pop()
            answer[node.val] = outside
            if node.left:
                left_outside = max(outside,
                                   depth + 1 + height.get(node.right, -1))
                stack.append((node.left, depth + 1, left_outside))
            if node.right:
                right_outside = max(outside,
                                    depth + 1 + height.get(node.left, -1))
                stack.append((node.right, depth + 1, right_outside))
        return [answer[value] for value in queries]

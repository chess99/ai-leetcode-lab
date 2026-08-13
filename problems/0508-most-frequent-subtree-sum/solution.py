# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:13:08Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        frequencies = Counter()
        sums = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                total = node.val + sums.get(node.left, 0) + sums.get(node.right, 0)
                sums[node] = total
                frequencies[total] += 1
                continue
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

        highest = max(frequencies.values())
        return [total for total, count in frequencies.items() if count == highest]

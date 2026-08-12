# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:52Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], sum: int) -> int:
        if not root:
            return 0
        frequencies = defaultdict(int)
        frequencies[0] = 1
        answer = 0
        stack = [(root, 0, False)]
        while stack:
            node, prefix, exiting = stack.pop()
            if exiting:
                frequencies[prefix] -= 1
                continue
            prefix += node.val
            answer += frequencies[prefix - sum]
            frequencies[prefix] += 1
            stack.append((node, prefix, True))
            if node.right:
                stack.append((node.right, prefix, False))
            if node.left:
                stack.append((node.left, prefix, False))
        return answer

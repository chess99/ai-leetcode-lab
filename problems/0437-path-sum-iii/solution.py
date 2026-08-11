# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:07Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1

        def dfs(node: Optional[TreeNode], prefix_sum: int) -> int:
            if node is None:
                return 0
            prefix_sum += node.val
            paths = prefix_counts[prefix_sum - targetSum]
            prefix_counts[prefix_sum] += 1
            paths += dfs(node.left, prefix_sum)
            paths += dfs(node.right, prefix_sum)
            prefix_counts[prefix_sum] -= 1
            return paths

        return dfs(root, 0)
